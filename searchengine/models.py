from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ' - ' + self.title