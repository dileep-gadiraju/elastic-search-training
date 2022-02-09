#  Aggregation Queries

```
 GET learn/_search
      {
        "_source": [],
        "size": 0,
        "min_score": 0.5,
        "query": {
          "bool": {
            "must": [],
            "filter": [],
            "should": [],
            "must_not": []
          }
        }
        , "aggs": {
          "Duration": {
            "terms": {
              "field": "duration",
              "order": {
                "_count": "asc"
              },
              "size": 10000
            }
          }
        }
```
