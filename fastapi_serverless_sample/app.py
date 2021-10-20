from fastapi import FastAPI
from mangum import Mangum
import os
import boto3


app = FastAPI()

stage = os.environ.get('STAGE', None)


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/users/user_id")
def read_item(user_id: int):
    table_name = os.environ.get('TABLE_NAME', '')
    table = boto3.resource("dynamodb", region_name='us-west-2').Table(table_name)
    response = table.get_item(
        Key={
            'PK': user_id
        }
    )

    return {"user_obj": response['Item']}


handler = Mangum(app)
