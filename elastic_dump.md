Refer [https://github.com/elasticsearch-dump/elasticsearch-dump](https://github.com/elasticsearch-dump/elasticsearch-dump) for installation and commands.

elasticdump \
  --input=http://localhost:9200/netflix_titles \
  --output=./netflix_titles_mapping.json \
  --type=mapping

elasticdump \
  --input=http://localhost:9200/netflix_titles \
  --output=./netflix_titles.json \
  --type=data

elasticdump \
  --input=http://localhost:9200/netflix_titles \
  --output=$ \
  | gzip > ./netflix_titles.json.gz

## Second Instance of Elastic and Kibana:
`docker network create elastic1`
`docker run -d --name es02-test --net elastic1 -p 127.0.0.1:9202:9200 -p 127.0.0.1:9302:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.17.0`
`docker run -d --name kib02-test --net elastic1  -p 127.0.0.1:5602:5601 -e "ELASTICSEARCH_HOSTS=http://es02-test:9202" docker.elastic.co/kibana/kibana:7.17.0`


# Copy an index from production to staging with analyzer and mapping:
elasticdump \
  --input=http://production.es.com:9200/netflix_titles \
  --output=http://staging.es.com:9200/netflix_titles \
  --type=analyzer
elasticdump \
  --input=http://production.es.com:9200/netflix_titles \
  --output=http://staging.es.com:9200/netflix_titles \
  --type=mapping
elasticdump \
  --input=http://production.es.com:9200/netflix_titles \
  --output=http://staging.es.com:9200/netflix_titles \
  --type=data