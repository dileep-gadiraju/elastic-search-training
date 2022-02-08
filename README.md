# Software Pre-Requisites
1. Python 3
2. Docker

# Install Elastic/ELK Search (as Docker Container)
Refer: https://www.elastic.co/guide/en/kibana/current/docker.html

1. Run `docker network create elastic`  to create docker network.
2. Run `docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.0` to pull elastic search docker image.
3. Run `docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.17.0`
   to run elastic search docker continer in single node mode.
4. If container succesfully starts , you should be able to access http://localhost:9200/

# Install Kibana(as Docker Container)

1. Run `docker pull docker.elastic.co/kibana/kibana:7.17.0` to pull kibana docker image.
2. Run `docker run --name kib01-test --net elastic -p 127.0.0.1:5601:5601 -e "ELASTICSEARCH_HOSTS=http://es01-test:9200" docker.elastic.co/kibana/kibana:7.17.0` to run kibana docker container.
3. If container succesfully starts , you should be able to access http://localhost:5601/


