import numpy as np
import pandas as pd

from elasticsearch import Elasticsearch
from elasticsearch import helpers
es_client = Elasticsearch(http_compress=True)

titanic_df = pd.read_csv("test.csv")

modifiedDataset=titanic_df.fillna("")

def doc_generator(df):
    df_iter = df.iterrows()
    for index, document in df_iter:
        yield {
                "_index": 'titanic_pandas_csv',
                "_type": "_doc",
                "_id" : f"{document['PassengerId']}",
                "_source": document.to_dict() ,
            }
    raise StopIteration

helpers.bulk(es_client, doc_generator(modifiedDataset))
