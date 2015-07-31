from elasticutils import S
from searchengine.models import LessonMapping


def search(text):
    s = S(LessonMapping)
    return s.query(title__match=text)
