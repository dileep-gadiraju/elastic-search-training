import sys,json
import os
import requests
from elasticsearch import Elasticsearch,helpers



res = requests.get('http://localhost:9200')
print (res.content)
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
path = './ab'
i = 0
for root, dirs, files in list(os.walk(path)):
    for name in files:
        print (os.path.join(root, name))
        with open(os.path.join(root, name), 'r') as json_file:
            data = json.load(json_file)
            #print(json.dumps(data, indent = 4))
            # data = json.load(f)
            # print(data)
            
             # Send the data into es
            es.index(index='metsa_index_v1', ignore=400, doc_type='docket',id=i, body=json.dumps(data, indent = 4))
            i = i + 1
