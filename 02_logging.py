import hazelcast
from fastapi import FastAPI
from models import Message

app = FastAPI()

hash_table = hazelcast.HazelcastClient().get_map('04map')


@app.post("/micro_hazelcast", status_code=200)
def handle_message(message: Message):
    hash_table.put(message.uuid, message.msg)
    print(message)


@app.get("/micro_hazelcast")
def return_messages():
    return hash_table.entry_set().result()
