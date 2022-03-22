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

Custom example with combination of above analyzers. 

  1. Try type as "keyword" without analyzer or text without analyzer for email field below.
  2. Normalizer to do case-insensitive search also included below.
  3. Custom Analyzer to strip HTML tags
  4. Stop Analyzer with custom stop words
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
                },
                "html_strip_analyzer": {
                  "type": "custom", 
                  "tokenizer": "standard",
                  "char_filter": [
                    "html_strip"
                  ],
                  "filter": [
                    "lowercase",
                    "asciifolding"
                  ]
                },
                "stop_analyzer": {
                  "type": "stop",
                  "stopwords": ["like","etc"]
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
          "email": {"type": "text" , "analyzer": "email_analyzer"},
          "profile_summary": {"type": "text", "analyzer": "html_strip_analyzer"}
        }
      }
    }

    POST /tarento-employees/_doc
    {
      "name": "Dinesh Karthik",
      "designation": "Data Architect",
      "contact": "91-9022330099",
      "dob": "02/07/1985",
      "email": "dinesh_karthik-02@tarento.com",
      "profile_summary": "Data Architect with experiance in <b>Azure Data Factory</b> , <b>Parquet</b>, <b>avro</b>."
    }

    POST /tarento-employees/_analyze
    {
      "analyzer": "html_strip_analyzer",
      "text":"Data Architect with experiance in <b>Azure Data Factory</b> , <b>Parquet</b>, <b>avro</b>."
    }

    POST /tarento-employees/_analyze
    {
      "analyzer": "stop_analyzer",
      "text":"Cloud data services like IaaS,PaaS etc."
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
                    "designation.normalize": "data arcHitect"
                  }
                } ,
                  {
                    "term": {
                      "profile_summary": "avro"
                    }
                  }                          
              ]
            }
          }
        }
```
