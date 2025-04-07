from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    in_stock: bool = True

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Get item by ID (dummy)
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "info": "This is a placeholder item"}

# Create new item (POST request)
@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item received", "item": item}

# Simple update (PUT)
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": f"Item {item_id} updated", "item": item}
