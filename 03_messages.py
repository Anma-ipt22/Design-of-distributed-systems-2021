from fastapi import FastAPI

app = FastAPI()


@app.get("/micro_hazelcast")
def root():
    return "Not implemented yet"
