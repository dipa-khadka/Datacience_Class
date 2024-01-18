import pickle
from pydantic import BaseModel

class Data(BaseModel):
    email : str
    
with open('spam_classifier.pickle','rb') as file:
    model = pickle.load(file)
    
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return{"msg":'Spam classifier model is running'}

@app.post("/classiify")
def classify(item:Data):
    y_pred = model.predict([item.email])
    return {'label': y_pred[0]}
