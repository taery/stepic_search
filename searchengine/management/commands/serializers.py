from rest_framework import serializers
from searchengine.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    # REP remove this and doesn't log problems on loading lessons or left? (raise_exception flag default value)
    def is_valid(self, raise_exception=True):
        return super().is_valid(raise_exception)

    class Meta:
        model = Lesson
        fields = ('id', 'title')
