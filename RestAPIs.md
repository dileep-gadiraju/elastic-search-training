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

* 