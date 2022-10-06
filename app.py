import json
import dbhelper
from flask import Flask, request

app = Flask(__name__)

@app.get('/api/item')
def get_all_items():
    all_items = dbhelper.run_statment('CALL all_items')
    if(type(all_items) == list):
        all_items_json = json.dumps(all_items, default=str)
        return all_items_json
    else:
        return 'sorry their was a problem'


@app.post('/api/post')
def post_create_item():
    item_name = request.json.get('item_name')
    item_description = request.json.get('item_description')
    item_stock = request.json.get('item_stock')
    create_item = dbhelper.run_statment('CALL create_item(?,?,?)', [item_name, item_description, item_stock])
    if(type(create_item) == list):
        create_item_json = json.dumps(create_item, default=str)
        return create_item_json
    else:
        return 'sorry their was a problem'


@app.post('/api/update')
def update_item():
    item_id = request.json.get('item_id')
    item_stock = request.json.get('item_stock')
    update_item = dbhelper.run_statment('CALL update_item(?,?)', [item_id, item_stock])
    if(type(update_item) == list):
        update_item_json = json.dumps(update_item, default=str)
        return update_item_json
    else:
        return 'sorry their was a problem'


@app.delete('/api/delete')
def delete_item():
    item_id = request.json.get('item_id')
    delete_item = dbhelper.run_statment('CALL delete_item(?)', [item_id])
    if(delete_item == True):
        return 'sucessfully deleted'
    else:
        return 'sorry their was a problem'


app.run(debug=True)