Refer 
    [Routing](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-shard-routing.html)
    [Customizing Document Routing](https://www.elastic.co/blog/customizing-your-document-routing)


Custom Routing with orders example:

```
DELETE /orders
    
PUT /orders
{
  "settings": {
    "number_of_shards": 5
  },
  "mappings": {
     "_routing": {
      "required": true 
    },
    "properties": {
      "customerName": {"type": "keyword"},
      "destAddress": { "type": "text" },
      "zip": { "type": "keyword" },
      "contact": { "type": "keyword" },
      "orderDate": {"type": "date", "format": "MM/dd/yyyy"},
      "itemType": {"type": "keyword"},
      "itemQty": {"type": "short"}
    }
  }
}

POST /orders/_doc?routing=560066 
{
  "customerName": "Gopal Rao",
  "destAddress": "Prestige Tranquility,F901,A4",
  "zip": "560066",
  "contact": "91-8193008312",
  "orderDate": "03/24/2022",
  "itemType": "EliteRusk0001",
  "itemQty": 5
}

POST /orders/_doc?routing=560043 
{
  "customerName": "Rammohan K",
  "destAddress": "85, Jayanti Nagar",
  "zip": "560043",
  "contact": "91-8100882212",
  "orderDate": "03/22/2022",
  "itemType": "ReynoldsPen10025",
  "itemQty": 2
}

POST /orders/_doc?routing=560062 
{
  "customerName": "Gopal Rao",
  "destAddress": "Prestige Tranquility,F901,A4",
  "zip": "560062",
  "contact": "91-9809128811",
  "orderDate": "03/20/2022",
  "itemType": "BoatRockerz-400",
  "itemQty": 1
}

GET /orders/_search?routing=560062
{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "zip": 560062
          }
        }
      ]
    }
  }
}

```



APIs to cat Shards/partitions.


```
GET /_cat/shards
GET /_cat/shards/orders
GET /_cat/shards/orders?h=index,shard,prirep,state,unassigned.reason
```

Reindexing API examples below. Refer [Reindex doc](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-reindex.html) for more details.
Creating `nyc-restaurants-reindexed` index with custom routing and invoking `_reindex` API from source index `nyc-restaurants`.
Below queries also indexes selective documents with ZIPCODE `match` query in source.
Also `max_docs` will limit number of documents from source to target index.


```

PUT /nyc-restaurants-reindexed
{
  "settings": {
    "number_of_shards": 10
  },  
  "mappings" : {
    "_routing": {
      "required": true 
    },
      "properties" : {
        "@timestamp" : {
          "type" : "date"
        },
        "ACTION" : {
          "type" : "text"
        },
        "BBL" : {
          "type" : "long"
        },
        "BIN" : {
          "type" : "long"
        },
        "BORO" : {
          "type" : "keyword"
        },
        "BUILDING" : {
          "type" : "keyword"
        },
        "CAMIS" : {
          "type" : "long"
        },
        "CRITICAL FLAG" : {
          "type" : "keyword"
        },
        "CUISINE DESCRIPTION" : {
          "type" : "keyword"
        },
        "Census Tract" : {
          "type" : "long"
        },
        "Community Board" : {
          "type" : "long"
        },
        "Council District" : {
          "type" : "long"
        },
        "DBA" : {
          "type" : "text"
        },
        "GRADE" : {
          "type" : "keyword"
        },
        "GRADE DATE" : {
          "type" : "date",
          "format" : "MM/dd/yyyy"
        },
        "INSPECTION DATE" : {
          "type" : "date",
          "format" : "MM/dd/yyyy"
        },
        "INSPECTION TYPE" : {
          "type" : "keyword"
        },
        "Latitude" : {
          "type" : "double"
        },
        "Longitude" : {
          "type" : "double"
        },
        "NTA" : {
          "type" : "keyword"
        },
        "PHONE" : {
          "type" : "keyword"
        },
        "RECORD DATE" : {
          "type" : "date",
          "format" : "MM/dd/yyyy"
        },
        "SCORE" : {
          "type" : "long"
        },
        "STREET" : {
          "type" : "keyword"
        },
        "VIOLATION CODE" : {
          "type" : "keyword"
        },
        "VIOLATION DESCRIPTION" : {
          "type" : "text"
        },
        "ZIPCODE" : {
          "type" : "long"
        },
        "borough" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "cuisine" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "grade" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "location" : {
          "type" : "geo_point"
        },
        "name" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
      }
    }
  }

GET /_cat/shards/nyc-restaurants-reindexed

POST _reindex
{
  "max_docs": 1145,
  "source": {
    "index": "nyc-restaurants",
    "slice": {
          "id": 0,
          "max": 2
    },    
    "query": {
      "match": {
        "ZIPCODE": "11211"
      }    
    }
  },
  "dest": {
    "index": "nyc-restaurants-reindexed",
    "routing": "=11211"
  }
}

POST _reindex
{
  "source": {
    "index": "nyc-restaurants",
    "slice": {
          "id": 0,
          "max": 4
    },    
    "query": {
      "match": {
        "ZIPCODE": "11004"
      }    
    }
  },
  "dest": {
    "index": "nyc-restaurants-reindexed",
    "routing": "=11004"
  }
}
```

Below search queries will includes `from` and `size` to paginate the documents.
`from` is the start index and `size` page size(number of documents in the page).


```
GET /nyc-restaurants-reindexed/_search
{
  "from": 1,
  "size": 5000
}

GET /nyc-restaurants-reindexed/_search?routing=11211
{
  "from": 1140,
  "size": 5000
}

GET /nyc-restaurants-reindexed/_search?routing=11004
{
  "from": 1,
  "size": 5000
}
```

Below queries you can search docs with only filtered path. `size=0` will skip documents and 
`filter_path=hits.total,_shards.successful` will only pull specificed two fields.

```
GET /nyc-restaurants-reindexed/_search
GET /nyc-restaurants-reindexed/_search?size=0&filter_path=hits.total,_shards.successful
```