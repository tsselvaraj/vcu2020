from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'tselvaraj',
    'text': 'VCU Text Analytics',
    'timestamp': datetime.now(),
    'building' : 'Business',
}
res = es.index(index="test", doc_type='testdoc', id=1, body=doc)
print(res)
