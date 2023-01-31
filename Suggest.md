#### Did you mean suggestions
1.  `Create idx_did_you_mean` index.
```
PUT idx_did_you_mean
{
  "settings": {
    "analysis": {
      "analyzer": {
        "shingle_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "shingle_filter"
          ]
        }
      },
      "filter": {
        "shingle_filter": {
          "type": "shingle",
          "min_shingle_size": 2,
          "max_shingle_size": 3
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "description": {
        "type": "text"
      },
      "title": {
        "type": "text",
        "fields": {
          "suggest": {
            "type": "text",
            "analyzer": "shingle_analyzer"
          }
        }
      },
      "year_release": {
        "type": "long"
      }
    }
  }
}
```

2.  Execute below query:

        ```
        GET idx_did_you_mean/_search
        {
        "suggest": {
            "text": "transformers revenge of the falen",
            "did_you_mean": {
            "phrase": {
                "field": "title.suggest",
                "size": 5
            }
            }
        }
        }
        ```
3.  