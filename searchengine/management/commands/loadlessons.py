import json
import os

import requests
from django.core.management.base import BaseCommand
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from searchengine.models import Lesson
from stepic_search.settings import STEPIC_API_URL


class Command(BaseCommand):
    help = 'Loads lessons titles from json'

    def add_arguments(self, parser):
        parser.add_argument('-f', dest='file')
        parser.add_argument('-p', type=int, dest='pages_count')

    def handle(self, *args, **options):
        if options.get('file'):
            file_to_load = os.path.abspath(options.get('file'))
            self.stdout.write("Loads lessons from file '{}'".format(file_to_load))
            json_load = json.loads(open(file_to_load).read())
            serialize_lessons(self, json_load)
        else:
            self.stdout.write("Load lessons from stepic.org".format(options))
            pages_count = options.get('pages_count')
            has_next = True
            current_page = 0
            while has_next:
                response = requests.get(form_next_url(current_page)).json()
                current_page = response['meta']['page']
                serialize_lessons(self, response)
                self.stdout.write("Page {} was loaded".format(current_page))
                has_next = response['meta']['has_next'] and (pages_count is None or current_page < pages_count)
        self.stdout.write('{} lessons now in database'.format(Lesson.objects.count()))


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title')


def form_next_url(current_page):
    return STEPIC_API_URL + '?page=' + str(current_page + 1)


def serialize_lessons(self, json_load):
    for elem in json_load['lessons']:
        serializer = LessonSerializer(data=elem)
        try:
            if serializer.is_valid():
                serializer.save()
        except ValidationError as e:
            self.stdout.write('Skip adding element {}: {}'.format(elem['id'], elem['title']))
            self.stderr.write('ValidationError: {}'.format(e.detail))
