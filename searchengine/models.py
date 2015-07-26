from django.db import models
# from elasticsearch import Elasticsearch


class Lesson(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ' - ' + self.title
