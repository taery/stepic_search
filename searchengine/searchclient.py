from elasticutils import S

from searchengine.models import LessonMapping


def search(text):
    s = S(LessonMapping)
    s = s.query_raw({
        "multi_match": {
            "query": text,
            "fields": ["title", "title.en", "title.ru"],
            "type": "most_fields"
        }
    })
    return s[:s.count()]
