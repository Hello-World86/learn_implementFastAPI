from fastapi import FastAPI
import json 

app = FastAPI()

def load_data():
    try:
        with open('patient_info.json', 'r') as f:
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