from django.core.management import BaseCommand
from searchengine.models import LessonMapping


class Command(BaseCommand):
    help = 'Creates lesson titles index'

    def handle(self, *args, **options):
        from searchengine.models import Lesson

        mapping = LessonMapping()
        es = mapping.get_es()
        es.indices.delete(index='lesson_index', ignore=404)
        es.indices.create(index='lesson_index')
        for lesson in Lesson.objects.all():
            entry = mapping.extract_document(lesson.id)
            es.index(index='lesson_index', doc_type='lesson-entry-type', body=entry)
