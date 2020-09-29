import json
from flask import Flask, request, Response
from pymongo import MongoClient
from bl import store_endpoint, get_all

app = Flask(__name__)


class Data:
    def __init__(self, data):
        self.__dict__ = data

    def json(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return ""

@app.route('/apis', methods=["GET", "POST"])
def hello_world():
    client = MongoClient()
    db = client.metaapi
    collection = db.apis

    d = {
        "name": "Anna",
        "age": 34
    }
    json_str = json.dumps(d)

    d_obj = Data(d)
    d_obj.json()

    # POST
    if request.method == "POST":
        data = json.loads(request.data)
        if data['type'].lower() == 'endpoint':
            return f'{{"id": {store_endpoint(data)}, "status": "Created"}}', 201
    else:  # GET
        return get_all(), 200


if __name__ == '__main__':
    app.run()
