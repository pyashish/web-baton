# Web-Baton


<img src="app/img/web-baton.jpg" height="250">

#### Webhook templatizations made stupid easy. 

v0.1.0: Supports for Headers & custom templates.


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
### Provide the server url in the webhook configuration

```server_url : https://web-baton-server:8000/web-baton``` 

Note: By default the server runs on port 8000. This is configurable.

