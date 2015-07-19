from django.db import models
from django_elasticsearch.models import EsIndexable


class Lesson(EsIndexable, models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ' - ' + self.title