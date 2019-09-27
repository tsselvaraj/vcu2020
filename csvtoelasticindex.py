from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch()

with open('test.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='titanic')
