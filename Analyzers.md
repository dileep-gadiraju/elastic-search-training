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

* One custom example with combination of above analyzers:
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
            }
        }
      },
      "mappings": {
        "properties": {
          "name": { "type": "text" },
          "designation": { "type": "keyword" },
          "contact": { "type": "keyword" },
          "dob": {"type": "date", "format": "MM/dd/yyyy"},
          "email": {"type": "text" , "analyzer": "email_analyzer"}
        }
      }
    }
```
