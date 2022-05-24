1. `pip3 install -r requirements.txt `
2. Simple search query

```
GET /metsa_index_v1/_search
{
  "size": 1000,
  "min_score": 0.5,
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "Items.Data.dimensions.Product Net Weight:": "1.28 kg"
          }
        }
      ]
    }
  } 
}
```


3. Search Query with AND

```
GET /metsa_data_v1/_search
{
  "size": 1000,
  "min_score": 0.5,
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "Items.Name": "AI620 Analog"
          }
        },{
          "match": {
            "Items.Data.additional-information.Product Type:": "I-O_Module"
          }
        }
      ]
    }
  } 
}
```