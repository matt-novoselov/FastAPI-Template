from fastapi import FastAPI
from config import ROOT_PATH

app = FastAPI(root_path=ROOT_PATH)


@app.get("/")
async def root():
    return {"message": "Hello World"}
