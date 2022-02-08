
# Kibana Queries

Refer https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html

* Basic queries (Level 1):
  * `GET _cat/indices`
  * `GET learn/_search`  to search learn index
  * `GET learn/_doc/{doc _id}` to search specific document in a index. Example `GET learn/_doc/zmUU2X4B7LKaS-lNQmJ3`
  * Basic query skeleton 
  ```
    GET learn/_search
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
       GET learn/_search
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
          GET learn/_search
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
    GET learn/_search
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


* Queries using NYC Restaurants:

`GET /nyc-restaurants/_search
{
  "query":{
    "match": {
      "cuisine": "Spanish"
    }
  }
}`

`

`



