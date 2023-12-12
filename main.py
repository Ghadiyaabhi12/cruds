from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()

fake_db = []

class Item(BaseModel):
    id: int
    name: str 
items = []

@app.get("/items", response_model=List[Item])
async def read_items():
    return items

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item
