from django.core.management.base import BaseCommand
from searchengine.models import Lesson


class Command(BaseCommand):
    help = 'Clears lessons db'

    def handle(self, *args, **options):
        lessons_count = Lesson.objects.count()
        Lesson.objects.all().delete()
        self.stdout.write('Delete {} lessons'.format(lessons_count))

