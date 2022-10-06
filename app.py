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


@app.patch('/api/update')
def update_items():
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

#-----------------------------------------------------------------------------

@app.get('/api/employee')
def get_employee_with_id():
    employee_id = request.args.get('employee_id')
    all_employees = dbhelper.run_statment('CALL get_employees(?)', [employee_id])
    if(type(all_employees) == list):
        all_employees_json = json.dumps(all_employees, default=str)
        return all_employees_json
    else:
        return 'sorry their was a problem'


@app.post('/api/employee/post')
def post_employees():
    employee_name = request.json.get('employee_name')
    employee_position = request.json.get('employee_position')
    employee_hourly_wage = request.json.get('employee_hourly_wage')
    create_employee = dbhelper.run_statment('CALL create_employee(?,?,?)', [employee_name, employee_position, employee_hourly_wage])
    if(type(create_employee) == list):
        create_employee_json = json.dumps(create_employee, default=str)
        return create_employee_json

app.run(debug=True)