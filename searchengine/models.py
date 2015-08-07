from django.db import models
from elasticutils.contrib.django import MappingType, Indexable


class Lesson(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return "{} lesson with id {}: {}".format("Public" if self.is_public else "Private", self.id, self.title)


class LessonMapping(MappingType, Indexable):
    @classmethod
    def get_index(cls):
        return 'lesson_index'

    @classmethod
    def get_mapping_type_name(cls):
        return 'lesson-entry-type'

    @classmethod
    def extract_document(cls, obj_id, obj=None):
        if obj is None:
            obj = cls.get_model().objects.get(pk=obj_id)
        return {
            'id': obj.id,
            'title': obj.title
        }

    @classmethod
    def get_model(cls):
        return Lesson

    def get_object(self):
        return self.get_model().objects.get(pk=self._id)

    @classmethod
    def get_mapping(cls):
        return {
            'lesson-entry-type': {
                'properties': {
                    'id': {'type': 'long', 'index': 'not_analyzed'},
                    'title': {
                        'type': 'string',
                        "fields": {
                            "en": {
                                "type": "string",
                                "analyzer": "english"
                            },
                            "ru": {
                                "type": "string",
                                "analyzer": "russian"
                            }
                        }
                    }
                }
            }
        }
