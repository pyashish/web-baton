# Web-Baton


<img src="app/img/web-baton.jpg" height="250">
Webhook templatization made easy. 


## Getting Started

### Dependencies 

Python >=3.6

### Installation
```python
pip install fastapi uvicorn
```

### Config

Populate config.json with headers & templatization.

```Example
{
  "url": "https://sample_url",
  "headers": {
      "X-HINT-TO-SERVER": "hint-id-example",
      "APP-KEY": "af23rkhf.kh230fhvskh2339fhs.asfj23091jf21l0svncy"
  },
  "payload_template": {
    "incident_name": "payloadKey",
    "incident_metadata" : {
      "my_custom_key": "payloadKey2",
      "properties": {
        "reason": "payloadKey3.payloadNestedKey"
      }
    }
  }
}
```
### Start the server

```bash
uvicorn baton:app --reload
```
