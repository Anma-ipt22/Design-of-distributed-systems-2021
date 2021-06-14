import uuid
import httpx
import json
from fastapi import FastAPI


app = FastAPI()


@app.post("/micro_basics", status_code=200)
def message_handler(text: str):
    id=str(uuid.uuid1())
    d=json.dumps({'id': id, 'msg': text})
    httpx.post('http://127.0.0.1:8081/micro_basics', data=d)


@app.get("/micro_basics")
def message_handler():
    logging_response = httpx.get('http://127.0.0.1:8081/micro_basics')
    messages_response = httpx.get('http://127.0.0.1:8082/micro_basics')
    return logging_response.text.strip('"') + messages_response.text.strip('"')
