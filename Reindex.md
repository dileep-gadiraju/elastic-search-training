```
GET mestro-app-logs-v2/_search
GET mestro-app-logs-v2/_mapping

PUT mestro-app-logs-v3
{
  "mappings" : {
      "properties" : {
        "agentId" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "buildNumber" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "jobId" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "jobType" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "message" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "password" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "timestamp" : {
          "type" : "long"
        },
        "docDate":{
          "type": "date"
        },
        "type" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "username" : {
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


POST _reindex
{
  "source": {
    "index": "mestro-app-logs-v2"
  },
  "dest": {
    "index": "mestro-app-logs-v3"
  },
   "script":{
      "lang":"painless",
      "source":"ctx._source.docDate= ctx._source.timestamp"
   }
}

GET /mestro-app-logs-v3/_search

GET /mestro-app-logs-v3/_search
{
  "query": {
    "range": {
      "docDate": {
        "gte": "now-120h",
        "lte": "now"
      }
    }
  }  
}

GET /mestro-app-logs-v3/_mapping
```