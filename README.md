# Software Pre-Requisites
1. Python 3
2. https://docs.conda.io/en/latest/
3. Docker

# Install Elastic/ELK Search (as Docker Container)
Refer: https://www.elastic.co/guide/en/kibana/current/docker.html

1. Run `docker network create elastic`  to create docker network. This is one time setup step.
2. Run `docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.0` to pull elastic search docker image.
3. Run `docker run --name es01-test --net elastic -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.17.0`
   to run elastic search docker continer in single node mode. If container with same name already exists , Run `docker rm es01-test` first.
4. If container succesfully starts , you should be able to access http://localhost:9200/

# Install Kibana(as Docker Container)

1. Run `docker pull docker.elastic.co/kibana/kibana:7.17.0` to pull kibana docker image.
2. Run `docker run --name kib01-test --net elastic  -p 127.0.0.1:5601:5601 -e "ELASTICSEARCH_HOSTS=http://es01-test:9200" docker.elastic.co/kibana/kibana:7.17.0` to run kibana docker container. If container with same name already exists , Run `docker rm kib01-test` first.
3. If container succesfully starts , you should be able to access http://localhost:5601/
4. TODO : -v /Users/dileep.gadiraju/projects/elk-search-training/kibana.yml:/usr/share/kibana/config/kibana.yml


# Working with Netflix dataset

1. Download netflix_titles.csv from https://www.kaggle.com/shivamb/netflix-shows into ./sample-data/ folder.
2. Navigae to kibana Dashboard Home page `http://localhost:5601/app/home#/`
3. Choose Upload a file option link to upload `netflix_titles.csv` file and Import the data as Index 'netflix'.
3. Navigate to kibana dashboard DevTools page. `http://localhost:5601/app/dev_tools#/console`
4. Refer [BasicQueries.md](/BasicQueries.md) for basic elastic search queries and try in above Kibana DevTools.
5. Refer [AggregationQueries.md](/AggregationQueries.md) for Aggregation queries.
6. Refer [GeoQueries.md](/GeoQueries.md) for Geo Queries.
7. Refer [Analyzers.md](/Analyzers.md)
8. Refer [Routing.md](/Routing.md) for Routing.


# Useful links:
1. http://localhost:5601/app/management/data/index_management/indices
2. 
