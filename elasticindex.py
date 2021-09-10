from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'TSS',
    'text': 'Sales',
    'timestamp': datetime.now(),
    'building' : 'House',
    'apt' : '10',
    'street' : 'Penn Street',
    'location' : 'Richmond VA',
}
res = es.index(index="vcu", doc_type='vcudoc', id=1, body=doc)
print(res)
