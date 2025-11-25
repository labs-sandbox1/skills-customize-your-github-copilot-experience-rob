from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# TODO: Implement CRUD endpoints for Item
# - POST /items
# - GET /items
# - GET /items/{id}
# - PUT /items/{id}
# - DELETE /items/{id}

# You can run this app with:
# uvicorn starter-code:app --reload
