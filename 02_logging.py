from fastapi import FastAPI
from pydantic import BaseModel


class Message(BaseModel):
    id: str
    msg: str


app = FastAPI()

hash_table = dict()


@app.post("/micro_basics", status_code=200)
def handle_message(message: Message):
    hash_table[message.id] = message.msg
    print(message)


@app.get("/micro_basics")
def return_messages():
    return ''.join(hash_table.values())
