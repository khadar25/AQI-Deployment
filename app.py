from flask import Flask,render_template,url_for,request
import pandas as pd 
import numpy as np

import pickle

# load the model from disk
pick = open('random_forest_regression_model.pkl', 'rb')
loaded_model=pickle.load(pick)
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')



@app.route('/predict',methods=['POST'])
def predict():
    value_T = request.form['T']
    value_TM = request.form['TM']
    value_Tm = request.form['Tm']
    value_H = request.form['H']
    value_VV = request.form['VV']
    value_v = request.form['v']
    value_vm = request.form['vm']
    values = np.array([value_T,value_TM,value_Tm,value_H,value_VV,value_v,value_vm])
    values = values.reshape(1, -1)
    #df=pd.read_csv('real_2018.csv')
    my_prediction=loaded_model.predict(values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)