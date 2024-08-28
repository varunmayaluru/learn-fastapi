from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import requests
import json
from pathlib import Path


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/hello-world")
def read_root():
    return {"message": "Welcome to FastAPI, Hello world"}

# print(read_root())

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Function to fetch JSON data from a local file
def fetch_json_data(file_path: str):
    # Construct the full path to the JSON file
    path = Path(file_path)

    # Check if the file exists
    if path.is_file():
        # Open and load the JSON file
        with open(path, 'r') as file:
            return json.load(file)
    else:
        # Return None if the file does not exist
        return None

# FastAPI route to fetch and return JSON data from a local file
@app.get("/get-person")
async def get_person():
    file_path = 'persons.json'  # Path to your local JSON file
    data = fetch_json_data(file_path)

    if data:
        return data
    else:
        raise HTTPException(status_code=500, detail="Failed to fetch data")

# Define a Pydantic model for the item
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# In-memory storage for items
items = {}

# Define a POST endpoint to create a new item
@app.post("/items/")
async def create_item(item: Item):
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")

    items[item.name] = item
    return {"message": "Item created successfully", "item": item}

# Run the app using: uvicorn filename:app --reload
