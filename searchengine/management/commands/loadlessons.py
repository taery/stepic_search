import json
import os

from django.core.management.base import BaseCommand
from rest_framework.exceptions import ValidationError

from searchengine.management.commands.serializers import LessonSerializer
from searchengine.models import Lesson


class Command(BaseCommand):
    help = 'Loads lessons titles from json'

    def add_arguments(self, parser):
        parser.add_argument('-f', dest='file')

    def handle(self, *args, **options):
        file_to_load = os.path.abspath(options.get('file'))
        if file_to_load:
            # TODO check that file is correct
            self.stdout.write("Loads lessons from file '{}'".format(file_to_load))
            json_load = json.loads(open(file_to_load).read())
        else:
            self.stdout.write("Run command {}".format(options))
            raise Exception('Not implemented yet')
        for elem in json_load['lessons']:
            serializer = LessonSerializer(data=elem)
            try:
                if serializer.is_valid():
                    serializer.save()
            except ValidationError as e:
                self.stdout.write('Skip adding element {}: {}'.format(elem['id'], elem['title']))
                self.stderr.write('ValidationError: {}'.format(e.detail))

        self.stdout.write('{} lessons now in database'.format(Lesson.objects.count()))