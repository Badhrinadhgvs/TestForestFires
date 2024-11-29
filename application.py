from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

application=Flask(__name__)
app = application

## import Ridge Regressor and Standard Scaler pkl

ridge_model=pickle.load(open('models/ridge.pkl','rb'))
scaler = pickle.load(open('models/scale.pkl','rb'))

@app.route("/",methods=['POST','GET'])
def index():
  if request.method == 'POST':
    t=int(request.form['Temperature'])
    rh = int(request.form['RH'])
    ws = int(request.form['WS'])
    rain = int(request.form['Rain'])
    ffmc=int(request.form['FFMC'])
    dmc=int(request.form['DMC'])
    isi=int(request.form['ISI'])
    classes=int(request.form['Classes'])
    region=int(request.form['Region'])
    pred=ridge_model.predict(scaler.transform([[t,rh,ws,rain,ffmc,dmc,isi,classes,region]]))
    pred=f"There is a chance of {int(np.round(pred))}% is there"
    return render_template('index.html',result=pred)
  return render_template('index.html')


if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)