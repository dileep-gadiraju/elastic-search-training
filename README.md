# Software Pre-Requisites
ElasticSearch , Kibana are deployed as Docker containers.
1. Docker.

# Install Elastic Search (as Docker Container)
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


# Explore ElasticSearch with Netflix,nyc-restaurants and other mock datasets.

1. Refer [netflix_titles.csv](/sample-data/netflix_titles.csv). Source : https://www.kaggle.com/shivamb/netflix-shows.
2. Navigae to kibana Dashboard Home page `http://localhost:5601/app/home#/`
3. Choose Upload a file option link to upload [netflix_titles.csv](/sample-data/netflix_titles.csv) file and Import the data as Index 'netflix'.
3. Navigate to Kibana dashboard [DevTools]((http://localhost:5601/app/dev_tools#/console)) page.
4. Also explore [nyc-restaurants.csv](/sample-data/nyc-restaurants.csv). 
   This dataset is used in below hands on examples. Please import this data also as `nyc-restaurants` index. 
5. After importing above datasets , open [Elastic Search Discover](http://localhost:5601/app/discover#) and select index you want to discover.
   Right side of Search box , you can choose `Syntax options` between `KQL` and `Lucene` for search.
6. Refer [BasicQueries](/BasicQueries.md) and try in Kibana dashboard [DevTools]((http://localhost:5601/app/dev_tools#/console)).
7. Refer [AggregationQueries](/AggregationQueries.md) for Aggregation queries.
8. Refer [GeoQueries](/GeoQueries.md) for Geo Queries.
9. Refer [Analyzers](/Analyzers.md)
10. Refer [Routing.](/Routing.md) for Routing.
11. Refer [OtherAPIs](/OtherAPIs.md).
12. Refer [DataStreams](/DataStreams.md).


# Runtime links:
1. http://localhost:5601/app/management/data/index_management/indices
2. http://localhost:5601/app/dev_tools#/console
3. http://localhost:5601/app/discover#