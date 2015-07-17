from django.core.management.base import BaseCommand
from django.core import serializers
from searchengine.models import Lesson

class Command(BaseCommand):
    help = 'Loads lessons titles from json'

    def add_arguments(self, parser):
        parser.add_argument('-f', dest='file')

    def handle(self, *args, **options):
        file_to_load = options.get('file')
        if file_to_load:
            self.stdout.write("Load file " + file_to_load)
            # TODO check that file is correct
            for obj in serializers.deserialize('json', open(file_to_load).read()):
                self.stdout.write(obj)
        else:
            self.stdout.write("Run command" + str(options))
