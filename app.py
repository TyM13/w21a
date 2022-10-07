import json
import dbhelper
from flask import Flask, request

app = Flask(__name__)

@app.get('/api/item')
def get_all_items():
#runs the run_statment from dbhelper and calls the procedure all_items and stores in as the variable all items
    all_items = dbhelper.run_statment('CALL all_items')
# checks to see if all items are == to a list
    if(type(all_items) == list):
# takes all_items and puts it in the format of json and if it can't convert, it will default to a string and store it in the variable all_items_json
        all_items_json = json.dumps(all_items, default=str)
#returns data as json
        return all_items_json
    else:
        return 'sorry their was a problem'


@app.post('/api/post')
def post_create_item():
# for getting the value that the client would of sent
    item_name = request.json.get('item_name')
    item_description = request.json.get('item_description')
    item_stock = request.json.get('item_stock')
    #runs the run_statment from dbhelper and calls the procedure create_item and stores in as the variable create_item and takes in the 3 variables for inputs
    create_item = dbhelper.run_statment('CALL create_item(?,?,?)', [item_name, item_description, item_stock])
# checks to see if all items are == to a list
    if(type(create_item) == list):
# takes create_item_json and puts it in the format of json and if it can't convert, it will default to a string and store it in the variable all_items_json
        create_item_json = json.dumps(create_item, default=str)
#returns data as json
        return create_item_json
    else:
        return 'sorry their was a problem'


@app.patch('/api/update')
def update_items():
# for getting the value that the client would of sent
    item_id = request.json.get('item_id')
    item_stock = request.json.get('item_stock')
    #runs the run_statment from dbhelper and calls the procedure update_item and stores in as the variable update_item and takes in the 3 variables for inputs
    update_item = dbhelper.run_statment('CALL update_item(?,?)', [item_id, item_stock])
# checks to see if all items are == to a list
    if(type(update_item) == list):
# takes update_item and puts it in the format of json and if it can't convert, it will default to a string and store it in the variable all_items_json
        update_item_json = json.dumps(update_item, default=str)
#returns data as json
        return update_item_json
    else:
        return 'sorry their was a problem'


@app.delete('/api/delete')
def delete_item():
# for getting the value that the client would of sent
    item_id = request.json.get('item_id')
#runs the run_statment from dbhelper and calls the procedure delete_item and stores in as the variable delete_item
    delete_item = dbhelper.run_statment('CALL delete_item(?)', [item_id])
# checks to see if all items are == to a list
    if(type(delete_item) == list):
# if delete item is == [0][0] no row or coloumn if will error else it will delete the item and return a success message
        if(delete_item[0][0] == 0):
            return 'sorry their was a problem'  
        else:
            return 'sucessfully deleted'

#----------------------------------------------------------------------------- same as above code

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


@app.patch('/api/employee/patch')
def update_employee():
    employee_id = request.json.get('employee_id')
    employee_hourly_wage = request.json.get('employee_hourly_wage')
    update_employee = dbhelper.run_statment('CALL update_employee_info(?,?)', [employee_id, employee_hourly_wage])
    if(type(update_employee) == list):
        update_employee_json = json.dumps(update_employee, default=str)
        return update_employee_json



@app.delete('/api/employee/delete')
def delete_employee():
    employee_id = request.json.get('employee_id')
    delete_employee = dbhelper.run_statment('CALL delete_employee(?)', [employee_id])
    if(type(delete_employee) == list):
        if(delete_item[0][0] == 0):
            return 'sorry their was a problem'  
    else:
        return 'sucessfully deleted' 



app.run(debug=True)