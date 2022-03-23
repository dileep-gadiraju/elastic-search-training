#  Aggregation Queries
Reference https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html

Navigate to [More ways to add data](http://localhost:5601/app/home#/tutorial_directory/sampleData) and `Add data` button on `Sample web logs` widget.
This will install `Sample web logs` dataset and stored as `kibana_sample_data_logs` index.

Now Navigate to [DevTools]((http://localhost:5601/app/dev_tools#/console)) and try below queries to checking mappings and documents in `kibana_sample_data_logs` index.

```
GET /kibana_sample_data_logs/_mapping
GET /kibana_sample_data_logs/_search
```

Below query shows total counts of the `clientip` address in the index `kibana_sample_data_logs`.

```
GET /kibana_sample_data_logs/_search
{ 
 "size": 0, 
 "aggs": {
  "ip_count": {
    "value_count": {
      "field": "clientip" 
    }
  }
}
}
```

## Filter Aggregation
Filter aggregation helps filter documents into single bucket. Metrics can be calculated within that bucket.

Navigate to [More ways to add data](http://localhost:5601/app/home#/tutorial_directory/sampleData) and `Add data` button on `Sample eCommerce orders` widget.
This will install `Sample eCommerce orders` dataset and stored as `kibana_sample_data_ecommerce` index.

Now Navigate to [DevTools]((http://localhost:5601/app/dev_tools#/console)) and try below queries to checking mappings and documents in `kibana_sample_data_ecommerce` index.

```
GET /kibana_sample_data_ecommerce/_mapping
GET /kibana_sample_data_ecommerce/_search
```

Below query shows gives average product price purchased by a user.

```
GET /kibana_sample_data_ecommerce/_search
{ 
 "size": 0, 
 "aggs": {
        "user_based_filter" : {
            "filter" : { 
              "term": { 
                "user": "mary"
              }
            },
            "aggs" : {
                "avg_price" : { 
                  "avg" : { 
                    "field" : "products.price"
                  } 
                }
            }
        }
  }
}
```

## Cardinality Aggregation

Below query to find unique sku's in the `kibana_sample_data_ecommerce` index.

```
GET /kibana_sample_data_ecommerce/_search
{
  "size": 0, 
  "aggs": {
      "unique_skus": {
        "cardinality": {
          "field": "sku"
        }
      }
  }
}
```