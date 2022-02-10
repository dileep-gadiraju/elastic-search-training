#  Other Rest APIs

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

