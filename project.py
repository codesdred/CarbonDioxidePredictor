from flask import Flask,render_template,redirect,request,url_for,jsonify
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from RegressionFinal import MLModel,giveX,giveY,giveName
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/prediction",methods=["GET","POST"])

def prediction():
    prediction_result = None

    if request.method == "POST":
        country5 = request.form['country']
        year5 = request.form['year']
        year5 = int(year5)
        x = giveX(country5)
        y = giveY(country5)
        name = giveName(country5)
        plt.xlabel("Year")
        plt.ylabel("CO2 emission(tonnes)")
        plt.title(name+" CO2 emission result")
        plt.plot(x,y,color='red')

        prediction_result = MLModel(country5 , year5)


    return render_template("form1.html",pre_text=prediction_result,name= plt.show())




if __name__=="__main__":
    app.run(debug=True)