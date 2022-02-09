
# Kibana Queries

Refer https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html

* Basic queries (Level 1):
  * `GET _cat/indices`
  * `GET netflix/_search`  to search learn index
  * `GET netflix/_doc/{doc _id}` to search specific document in a index. Example `GET netflix/_doc/zmUU2X4B7LKaS-lNQmJ3`
  * Basic query skeleton 
  ```
    GET netflix/_search
    {
      "_source": [],
      "size": 20, 
      "min_score": 0.5,      
      "query":{
        "bool":{
          "must": [],
          "filter": [],
          "should": [],
          "must_not": []
        }
      }
    }
    ```
 * Example of AND query using must[] query :
    ```
       GET netflix/_search
                        {
                          "_source": ["country","director","rating","release_year","title"],
                          "size": 1000, 
                          "min_score": 0.5,
                          "query":{
                                        "bool":{
                                          "must": [
                                            {
                                              "match": {
                                                "title": "Nazi"
                                              }
                                            },
                                            {
                                              "match": {
                                                "title": "Camps"
                                              }
                                            }                    
                                            ],
                                          "filter": [],
                                          "should": [],
                                          "must_not": []
                                        }
                                      }
                        }
      ```

* Example OR query using should[] , NOT using must_not[] :
  ```
          GET netflix/_search
             {
                                          "_source": ["country","director","rating","release_year","title"],
                                          "size": 1000, 
                                          "min_score": 0.5,
                                          "query":{
                                                        "bool":{
                                                          "must": [
                                                            {
                                                              "match": {
                                                                "title": "Nazi"
                                                              }
                                                            },
                                                            {
                                                              "match": {
                                                                "title": "Camps"
                                                              }
                                                            }                    
                                                            ],
                                                          "filter": [],
                                                          "should": [],
                                                          "must_not": [{
                                                                  "match": {
                                                                    "title": "Mega"
                                                                  }
                                                                }]
                                                        }
                                                      }
               }
    ```

* Example of match_phrase:
    ```
    GET netflix/_search
                      {
                        "_source": ["country","director","rating","release_year","title"],
                        "size": 1000, 
                        "min_score": 0.5,
                        "query":{
                          "match_phrase": {
                            "title": "Extreme Survival"
                          }
                        }
                      }
    ```
* Example of filter with `term` and `range` clauses. Filter The filter parameter indicates filter context. They will filter out documents which do not match, but they will not affect the score for matching documents :
    ```
      
    ```
* Example of Nested boolean queries. Below query searchs for docs with Title has King or Nazi  and Title not having "Peking" and "Jack" :
    ```
      GET netflix/_search
      {
        "_source": [
          "title"
        ],
        "size": 20,
        "min_score": 0.5,
        "query": {
          "bool": {
            "must": [],
            "filter": [],
            "should": [
              {
                "match": {
                  "title": "King"
                }
              },
              {
                "match": {
                  "title": "Nazi"
                }
              }
            ],
            "must_not": [
              {
                "bool": {
                  "should": [
                    {
                      "match": {
                        "title": "Peking"
                      }
                    },
                    {
                      "match": {
                        "title": "Jack"
                      }
                    }
                  ]
                }
              }
            ]
          }
        }
      }
    ```