* Find nyc restaurants using `geo_distance` of 50 miles from location lat , long. Try changing distance to see the number of documents returned:


```
      GET nyc-restaurants/_search
      {
        "query": {
            "bool": {
            "filter": [
                {
                "geo_distance": {
                    "distance":"50",
                    "location": {
                    "lat": 40.680684493111,
                    "lon": -73.842623752253
                    }
                }
                }
            ]
            }
        }
      }
```


*  Find nyc restaurants using `geo_polygon`:
```
        GET nyc-restaurants/_search
         {
          "query": {
            "bool": {
              "filter": [
                {
                  "geo_polygon": {
                    "location": {
                      "points": [
                        {
                          "lat": 40.680684493111,
                          "lon": -73.5
                        },
                        {
                          "lat": 42.1219223,
                          "lon": -76.0051192
                        },
                        {
                          "lat": 41.7172748,
                          "lon": -73.5112227
                        },
                        {
                          "lat": 43.0761737,
                          "lon": -72.9673994
                        },
                        {
                          "lat": 43.3204449,
                          "lon": -75.1152266
                        }
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
```

* Explore other geo based searches using `geo_shape` , `geo_bounding_box` , `geo_distance_range` @ (Geo Queries)[https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-queries.html].
