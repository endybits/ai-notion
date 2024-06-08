import os
from fastapi import FastAPI
from notion_client import Client

from config.config import get_config_keys

keys = get_config_keys()
NOTION_TOKEN = keys["notion"]["token"]
OPENAI_API_KEY = keys["openai"]["api_key"]
os.environ["NOTION_TOKEN"] = NOTION_TOKEN
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
notion = Client(auth=os.environ["NOTION_TOKEN"])
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def read_health():
    return {"status": "ok"}

@app.get("/auth")
def read_auth():
    users = notion.users.list()
    return {
        "users": users
    }