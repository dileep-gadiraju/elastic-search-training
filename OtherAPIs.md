#  Other Rest APIs

Most Elasticsearch APIs accept an alias in place of a data stream or index name. You can change the data streams or indices of an alias at any time. If you use aliases in your application's Elasticsearch requests, you can reindex data with no downtime or changes to your app's code.

* Create _aliases for index and use it :
```
    POST /_aliases
    {
        "actions":{
            "add": {
                "index": "nyc-restaurants",
                "alias":"newyork-restaurants"
            }
        }
    }

    GET /newyork-restaurants/_search
    {
    "query": {
        "bool": {
        "must": [
            {"match": 
            {
            "ZIPCODE": 10458
            }
            }
        ]
        }
    }
    }
```

* Remove Aliases :

```
POST /_aliases
{
      "actions":{
        "remove": {
            "index": "nyc-restaurants",
            "alias":"newyork-restaurants"
        }
    }
}
```

* Create filtered _aliases and use it:
```
POST /_aliases
{
    "actions":{
        "add": {
            "index": "nyc-restaurants",
            "alias":"newyork-restaurants",
            "filter": 
              {
                "term": {
                  "GRADE": "C"
                }
              }
        }
    }
}

GET /newyork-restaurants/_search

```

* Create _alias combining multiple indecies:

```
POST /_aliases
{
 "actions": [{ 
     "add": {
          "alias": "netflix-nyc-rest", "indices": [ "netflix","nyc-restaurants" ]
        }  
  }]
}

GET /netflix-nyc-rest/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "_index": "nyc-restaurants"
          }
        }
      ]
    }
  }
}

```

CAT(Compact Aligned Text) APIs. Refer `https://www.elastic.co/guide/en/elasticsearch/reference/current/cat.html` for more details.
 
```
GET /_cat
GET _cat/indices?format=json&pretty
GET /_cat/aliases?format=json&pretty
GET /_cat/health?format=json&pretty
GET /_cat/nodeattrs?format=json&pretty
GET _cat/nodes?h=ip,port,heapPercent,name&format=json&pretty
GET /_cat/indices?format=json&pretty
GET _cat/templates?v=true&s=order:desc,index_patterns
GET _cat/aliases?format=json&pretty
GET /_cat/allocation?v=true&format=json&pretty
```

Mapping,setting,doc and analyze apis.

```
GET /_all/_mapping
GET /<index name>/_settings
POST /<index name>/_doc
```