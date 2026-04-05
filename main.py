from fastapi import FastAPI, Path, HTTPException, Query
import json 

app = FastAPI()

def load_data():
    try:
        with open('patient.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "patient_info.json was not found"}

    return data

@app.get("/")
def hello():
    return {'message' : 'Patient Management System'}

@app.get('/about')
def about():
    return{'message' : 'This is a fully functional patient management system developed with the implementation of the concept of fast api. '
    'This application will have four endpoints viz GET, POST, PUT and DELETE which aim to make record keeping, retrieval, updation and deletion proceeses of patients more manageable, organised, secure and available whenever needed.'}

@app.get('/view')
def view():
    data = load_data()
    return data

#Implementation of conceot of Path parameter to provide document example
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB',
example = 'P001')):
    #load all the patient's data at first
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail ='Patient doesnot exist in the system.')
#Use required as well as default query parameter to sort patient info 
@app.get('/sort')
def sort_patient_info(sort_by: str= Query(..., description='Sort on the basis of height, weight or bmi'), 
order: str = Query('asc', description = 'sort either in an ascending or descending order')):
    
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail=f'Invalid field selected from {valid_fields}')

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse= sort_order)

    return sorted_data