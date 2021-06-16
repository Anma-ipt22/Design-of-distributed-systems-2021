import uuid
import requests
import json
from random import choice
from fastapi import FastAPI
from models import FacadePostMessage

app = FastAPI()

LOGGING_SERVICES = ('http://127.0.0.1:8081/micro_hazelcast',
                                      'http://127.0.0.1:8001/micro_hazelcast',
                                      'http://127.0.0.1:8002/micro_hazelcast',
                                     )

def get_logging():
    return random.choice(LOGGING_SERVICES)

@app.post("/micro_hazelcast", status_code=200)
def message_handler(msg: FacadePostMessage):
    requests.post(url=get_logging(), json={'uuid': str(uuid.uuid1()), 'msg': msg.msg})


@app.get("/micro_hazelcast")
def message_handler():
    logging_response = requests.get(get_logging())
    messages_response = requests.get('http://127.0.0.1:8082/micro_hazelcast')
    return logging_response.text.strip('"') + " " + messages_response.text.strip('"')
