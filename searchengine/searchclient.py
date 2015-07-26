import json
import requests


def search(text):
    # client = Elasticsearch()
    # s = Search(client)
    # s.query('match', title=text)
    # response = s.execute()
    # return response.to_dict()
    data = {
        "query": {
            "query_string": {"query": text}
        }
    }

    response = requests.post('http://127.0.0.1:9200/lesson_index/lesson/_search', data=json.dumps(data))

    hits = response.json()['hits']['hits']
    resp = list()
    for hit in hits:
        l = dict()
        l['id'] = hit['_id']
        l['title'] = hit['_source']['title']
        resp.append(l)
    return resp