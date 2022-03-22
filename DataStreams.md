Refer `https://www.elastic.co/guide/en/elasticsearch/reference/current/data-streams.html`


APIs related to data streams:

```
GET /_ilm/policy
GET /_index_template
GET /_data_stream
```


Step#1 : Create ILM Policy to manage underlying indecies. Below policy , index rollover when shard size reaches 50 GB.
Index will be deleted when it reaches age of 60 days.

```
PUT /_ilm/policy/custom-policy-60dretention
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_size": "50GB"
          }
        }
      },
      "delete": {
        "min_age": "60d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}
```


Step#2 : Create index template for the data stream with above created ILM policy `custom-policy-60dretention`. Every document indexed to a data stream must contain a @timestamp field, mapped as a date or date_nanos field type. You can find mapping for the same in below index template. The “data_stream”:{} object indicates that it is a data stream and not a regular index.


```
PUT /_index_template/custom-logs-data-stream
{
  "index_patterns": [ "logs-data-stream*" ],
  "data_stream": { },
  "priority": 500,
  "template": {
	"settings": {
  	    "index.lifecycle.name": "custom-policy-60dretention"
	},
	"mappings":{
  	    "properties": {
    	        "@timestamp":{
      	      "type":"date"
    	        }
  	    }
	}
  }
}
```

Step#3 : First index request on `custom-logs-data-stream` will create Data Stream. Index template set above will make sure Data Stream is created instead of regular Index.

```
POST /custom-logs-data-stream/_doc/
{
  "@timestamp": "2021-04-07T12:02:15.000Z",
  "message": "Hello world"
}
POST /custom-logs-data-stream/_doc/
{
  "@timestamp": "2021-04-07T12:02:16.000Z",
  "message": "Hello world1"
}
POST /custom-logs-data-stream/_doc/
{
  "@timestamp": "2021-04-07T12:02:17.000Z",
  "message": "Hello world2"
}
```

Step#4 : Search Request on `custom-logs-data-stream` to fetch stream data.

```
GET /custom-logs-data-stream/_search

GET /custom-logs-*/_search

GET /custom-logs-*/_search
{
 "query": {
    "match": {
      "message": "world1"
    }
  }
}
```

Step#5 : Try `_delete_by_query` API with criteria

```
POST /custom-logs-data-stream/_delete_by_query
{
  "query": {
    "match": {
      "message": "world1"
    }
  }
}
```

Step#6 : Try deleting entire data stream and underlying indecies.

```
DELETE /_data_stream/custom-logs-data-stream
```

Step#7 : Try document delete using underlying index name and document id. You can find specific document to be deleted using below search API.

```
GET /custom-logs-data-stream/_search
{
  "query": {
    "match": {
      "message": "Hello world"
    }
  }
}


DELETE /custom-logs-data-stream/_doc/<_id>
DELETE /custom-logs-data-stream/_doc/cblUrH8BTpoOnKxgxuSe
```

Step#7:  DataStream are not meant for updates , but in extreme cases use below APIs to fetch `_seq_no`,`_primary_term`,`_id` and use 
`_doc` API for updating the doc. 


```
GET /custom-logs-data-stream/_search
{
  "seq_no_primary_term": true,
  "query": {
    "match": {
      "message": "Hello world"
    }
  }
}

PUT custom-logs-data-stream/_doc/crlVrH8BTpoOnKxgBuTD?if_seq_no=1&if_primary_term=1
{
  "@timestamp": "2020-03-07T12:02:07.000Z",
    "message": "Updated the document"
}

GET /custom-logs-data-stream/_search
```

