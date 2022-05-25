from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200')

resp = es.search(index="metsa_index_v1", query={"match": {"Items.Data.general.Product ID:":"3BHT300005R1"}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print(hit["_source"]["Items"][0]["Name"])
    print(hit["_source"]["Items"][0]["Url"])
    print(hit["_source"]["Items"][0]["Data"]["additional-information"])