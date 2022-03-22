
# Basic Queries

Refer https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html

* Basic APIs:

  * `GET _cat/indices`
  * `GET netflix/_search`  to search or learn index
  * `GET netflix/_doc/{doc _id}` to search specific document in a index. Example `GET netflix/_doc/zmUU2X4B7LKaS-lNQmJ3`
  * `GET /nyc-restaurants/_mapping/` to list/print mapping of given index `nyc-restaurants`
  * `GET /_all/_mapping` to list/print mapping of all indices.
  
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

 * Example of AND using must[] query :
 
```
GET netflix/_search
{
  "_source": [
    "country",
    "director",
    "rating",
    "release_year",
    "title"
  ],
  "size": 1000,
  "min_score": 0.5,
  "query": {
    "bool": {
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
  "_source": [
    "country",
    "director",
    "rating",
    "release_year",
    "title"
  ],
  "size": 1000,
  "min_score": 0.5,
  "query": {
    "bool": {
      "must": [],
      "filter": [],
      "should": [{
          "match": {
            "title": "Nazi"
          }
        },
        {
          "match": {
            "title": "Camps"
          }
        }],
      "must_not": [
        {
          "match": {
            "title": "Mega"
          }
        }
      ]
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

* Example of filter with `term` and `range` clauses. Filter indicates filter context. They will filter out documents which do not match, but they will not affect the score for matching documents :

```
GET /netflix/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "title": "prime"
          }
        }
      ]
    }
  }
}

GET /netflix/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "release_year": {
              "gte": 2000,
              "lte": 2010
            }
          }
        }
      ]
    }
  }
}

```

* Example of Nested boolean queries. Below query searchs for docs where title has King or Nazi  and title not having "Peking" or "Jack" :


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

* Create a new index with mappings and add documents.

```
PUT /tarento-employees
{
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "properties": {
      "name": { "type": "text" },
      "designation": { "type": "keyword" },
      "contact": { "type": "keyword" },
      "dob": {"type": "date", "format": "MM/dd/yyyy"}
    }
  }
}
POST /tarento-employees/_doc
{
  "name": "Dinesh Karthik",
  "designation": "Data Architect",
  "contact": "91-9022330099",
  "dob": "02/07/1985"
}
GET /tarento-employees/_search
```