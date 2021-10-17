from fastapi import FastAPI
from mangum import Mangum
import os
app = FastAPI(root_path="/dev/")

stage = os.environ.get('STAGE', None)



@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_item(item_id: int):
    return {"user_id": item_id}

handler = Mangum(app)