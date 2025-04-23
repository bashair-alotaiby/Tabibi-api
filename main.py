
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Tabibi API"}

@app.get("/glossary")
def read_glossary():
    with open("glossary.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
