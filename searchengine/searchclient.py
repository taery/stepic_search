from elasticutils import S
from searchengine.models import LessonMapping


def search(text):
    s = S(LessonMapping)
    s = s.query(title__match=text)
    return s[:s.count()]
