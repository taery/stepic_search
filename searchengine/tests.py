from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command

from searchengine.models import Lesson


class LoadLessonsTest(TestCase):

    def test_correct_load_lessons(self):
        out = StringIO()
        call_command('loadlessons', '-fsearchengine/testdata/several_lessons.json', stdout=out)
        self.assertIn('3 lessons now in database', out.getvalue())
        self.assertEqual(3, Lesson.objects.count(), 'Wrong lessons count after loading')

    def test_correct_double_loading(self):
        out = StringIO()
        call_command('loadlessons', '-fsearchengine/testdata/several_lessons.json', stdout=out)
        call_command('loadlessons', '-fsearchengine/testdata/several_lessons.json', stdout=out)
        self.assertIn('3 lessons now in database', out.getvalue())
        self.assertEqual(3, Lesson.objects.count(), 'Wrong lessons count after loading')

    def test_correct_ids(self):
        out = StringIO()
        call_command('loadlessons', '-fsearchengine/testdata/several_lessons.json', stdout=out)
        self.assertEqual(Lesson.objects.get(id=1), Lesson(id=1, title='A Journey of a Thousand Miles. . .'),
                         'Wrong lesson with id=1')
        self.assertRaises(Lesson.DoesNotExist, lambda: Lesson.objects.get(id=2))
        self.assertEqual(Lesson.objects.get(id=5), Lesson(id=5, title='Hidden Messages in the Replication Origin'),
                         'Wrong lesson with id=5')


class ClearLessonsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        call_command('loadlessons', '-fsearchengine/testdata/several_lessons.json')

    def test_remove_all_lessons(self):
        out = StringIO()
        call_command('clearlessons', stdout=out)
        self.assertIn('Delete 3 lessons', out.getvalue())