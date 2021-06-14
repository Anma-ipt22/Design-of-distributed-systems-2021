from fastapi import FastAPI

app = FastAPI()


@app.get("/micro_basics")
def root():
    return "Not implemented yet"
