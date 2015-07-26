from django.core.management import BaseCommand
from searchengine.models import Lesson

data = {
    "settings": {
        "number_of_shards": 4,
        "number_of_replicas": 1
    },
    "mappings": {
        "lesson": {
            "properties": {
                "title": {"type": "string", "boost": 4},
            }
        }
    }
}


class Command(BaseCommand):
    help = 'Creates lesson titles index'

    def handle(self, *args, **options):
        import json, requests

        response = requests.put('http://127.0.0.1:9200/lesson_index/', data=json.dumps(data))
        self.stdout.write(response.text)

        model_data = ''
        for l in Lesson.objects.all():
            model_data += '{"index": {"_id": "%s"}}\n' % l.pk
            model_data += json.dumps({
                "title": l.title,
            })+'\n'
        response = requests.put('http://127.0.0.1:9200/lesson_index/lesson/_bulk', data=model_data)
        self.stdout.write(response.text)