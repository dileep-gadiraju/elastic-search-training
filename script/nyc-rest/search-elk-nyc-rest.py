import elasticsearch

client = elasticsearch.Elasticsearch("http://localhost:9200")
resp = client.search(
    index="nyc-restaurants",
    size=0,
    body={
        "aggs": {
            "borough": {
                "terms": {
                    "field": "borough"
                },
                "aggs": {
                    "grades": {
                        "terms": {
                            "field": "grade"
                        }
                    }
                }
            }
        }
    }
)
print(resp)