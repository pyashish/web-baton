from typing import Optional

from fastapi import Body, FastAPI, Request, Response, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.routing import APIRoute
import requests
import json
app = FastAPI( title="Web-Baton",
    description="Project to relay the webhook baton to the target server with headers and template customization.",
    version="v0.1.0",)

class Resp(BaseModel):
    url: str
    payload: Optional[dict]
    headers: dict


@app.post("/web-baton", response_model=Resp)
async def baton(req : Request):
    config_json = _load_json()
    if not config_json:
        return JSONResponse(status_code=500,
                            content={"message": "Invalid Json, please correct the config file to json format."})
    if not bool(config_json['url']):
        return JSONResponse(status_code=500,
                            content={"message": "Please provide URL in the config"})
    headers = None
    try:
        data = await req.json()
    except json.decoder.JSONDecodeError:
        return "Invalid Json request."
    if bool(config_json['headers']):
        headers = config_json['headers']

    if bool(config_json['payload_template']):
        data = _extract_template(config_json['payload_template'], data)

    if not headers:
        resp = requests.post(url=config_json['url'], data=json.dumps(data))
    else:
        resp = requests.post(url=config_json['url'], data=json.dumps(data),
                          headers=headers)
    if resp.ok:
        if not headers:
            headers = ''
        return  {"url": config_json['url'],
                 "payload": data,
                 "headers": headers}
    else:
        return JSONResponse(status_code=500,
                            content={"message": "Error processing the payload data"})


def _load_json():
    with open('config.json', 'r+') as fp:
        try:
            json_object = json.load(fp)
        except ValueError as e:
            return False
        return json_object


def _extract_template(template, data):
    extract = {}
    for k,v in template.items():
        if type(v) is dict:
            extract[k] = _extract_template(v, data)
        if type(v) is str:
            nested_dict = v.split('.')
            if len(nested_dict) > 1:
                #TODO validate key/value exists
                extract[k] = data[nested_dict[0]][nested_dict[1]]
            else:
                extract[k] = data[v]
    return extract
