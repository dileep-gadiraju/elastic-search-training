Refer 
    [Routing](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-shard-routing.html)
    [Customizing Document Routing](https://www.elastic.co/blog/customizing-your-document-routing)

```
DELETE /orders
    
PUT /orders
{
  "settings": {
    "number_of_shards": 5
  },
  "mappings": {
     "_routing": {
      "required": true 
    },
    "properties": {
      "customerName": {"type": "keyword"},
      "destAddress": { "type": "text" },
      "zip": { "type": "keyword" },
      "contact": { "type": "keyword" },
      "orderDate": {"type": "date", "format": "MM/dd/yyyy"},
      "itemType": {"type": "keyword"},
      "itemQty": {"type": "short"}
    }
  }
}

POST /orders/_doc?routing=560066 
{
  "customerName": "Gopal Rao",
  "destAddress": "Prestige Tranquility,F901,A4",
  "zip": "560066",
  "contact": "91-8193008312",
  "orderDate": "03/24/2022",
  "itemType": "EliteRusk0001",
  "itemQty": 5
}

POST /orders/_doc?routing=560043 
{
  "customerName": "Rammohan K",
  "destAddress": "85, Jayanti Nagar",
  "zip": "560043",
  "contact": "91-8100882212",
  "orderDate": "03/22/2022",
  "itemType": "ReynoldsPen10025",
  "itemQty": 2
}

POST /orders/_doc?routing=560062 
{
  "customerName": "Gopal Rao",
  "destAddress": "Prestige Tranquility,F901,A4",
  "zip": "560062",
  "contact": "91-9809128811",
  "orderDate": "03/20/2022",
  "itemType": "BoatRockerz-400",
  "itemQty": 1
}

GET /orders/_search?routing=560062
{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "zip": 560062
          }
        }
      ]
    }
  }
}


GET /_cat/shards
GET /_cat/shards/orders
```

