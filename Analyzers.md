Refer [Analyzers Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-analyzers.html) for various types of analyzers.

* [Standard Analyzer](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-standard-analyzer.html)
* [Simple Analyzer](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-simple-analyzer.html)
* [Whitespace Analyzer](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-whitespace-analyzer.html)
* [Stop Analyzer](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-stop-analyzer.html)
* [Keyword Analyzer](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-keyword-analyzer.html)
* [Pattern Analyzer](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-pattern-analyzer.html)
* [Language Analyzers](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-lang-analyzer.html)
* [Fingerprint Analyzer](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-fingerprint-analyzer.html)
* [Custom Analyzers](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/analysis-custom-analyzer.html)

* One custom example with combination of above analyzers. 
  1. Try type as "keyword" without analyzer or text without analyzer for email field below.
  2. Normalizer to do case-insensitive search also included below.
```
PUT /tarento-employees
    {
      "settings": {
        "number_of_shards": 1,
        "analysis":{
            "analyzer":{
              "email_analyzer": {
                "type":      "pattern",
                "pattern":   "\\W|_", 
                "lowercase": true
                }
            },
            "normalizer": {
              "my_normalizer": {
                "type": "custom",
                "filter": ["lowercase"]
              }
            } 
        }
      },
      "mappings": {
        "properties": {
          "name": { "type": "text" },
          "designation": { 
            "type": "keyword",
              "fields": {
                  "normalize": {
                    "type": "keyword",
                    "normalizer": "my_normalizer"
                  },
                "keyword" : {
                  "type": "keyword"
                }
              }
          },
          "contact": { "type": "keyword" },
          "dob": {"type": "date", "format": "MM/dd/yyyy"},
          "email": {"type": "text" , "analyzer": "email_analyzer"}
        }
      }
    }

    POST /tarento-employees/_doc
    {
      "name": "Dinesh Karthik",
      "designation": "Data Architect",
      "contact": "91-9022330099",
      "dob": "02/07/1985",
      "email": "dinesh_karthik-02@tarento.com"
    }


GET /tarento-employees/_search
    {
      "query": {
        "bool": {
          "filter": [
            {
              "term": {
                "email": "karthik"
              }
            },
            {
              "term": {
                "designation.normalize": "data architect"
              }
            }            
          ]
        }
      }
    }
```
