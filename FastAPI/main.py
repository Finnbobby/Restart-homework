from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

# The @ is a decorator
#uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Item(BaseModel):
    name:str
    price:float

@app.get("/items/{item_id}")
def read_item(item_id: int, item: Item, item2: Item, q: Union[str, None] = None):
        print("hello line")
        return {"item_id": item_id, "q": q, "item": item, "item2": item2}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}