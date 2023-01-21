#### Correcting typos and spelling mistakes using Elasticsearch
1. From kibana dashobard , load sample [eCommerce] Revenue Dashboard
2. Navigate to [dev_tools console](http://localhost:5601/app/dev_tools#/console)
3. Try below queries for typo/spell corrections and you may notice search results with auto correct spellings.
   ```
        #Fuzzy Query
        POST kibana_sample_data_ecommerce/_search
        {
        "query": {
            "fuzzy": {
            "manufacturer": "Elitelligance"
            }
        }
        }
   ```
   ```
        #Fuzzy Match Query
        POST kibana_sample_data_ecommerce/_search
        {
        "query": {
            "match": {
            "customer_full_name": {
                "query" : "Mery Baeley",
                "fuzziness": "AUTO",
                "operator": "and"
            }
            }
        }
        }
   ```

