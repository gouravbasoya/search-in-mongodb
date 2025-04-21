from fastapi import FastAPI,Query
from pymongo import MongoClient

app=FastAPI()

client=MongoClient("mongodb://localhost:27017")
db=client["employees"]
collection=db["grocery"]

@app.get("/")
def home():
    return {"message":"hello"}

@app.get("/search")
def search_item(q:str= Query(...,description="product search term")):
    regex_query={"search_tags":{"$regex":q, "$options":"i"}}
    results=list(collection.find(regex_query,{"_id":0}))
    return {"results":results}