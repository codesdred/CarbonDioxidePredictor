import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def MLModel(country, year):
    dataset = pd.read_csv('emissiondata.csv')
    dataset.replace('NaN', np.nan, inplace=True)
    dataset.replace(np.nan, 0, inplace=True)
    dataset = dataset.loc[dataset["CO2 emission (Tons)"] != 0]
    
    newdata = dataset.loc[dataset["Code"] == country]
    
    if newdata.empty:
        return "Country Data Not Available"  # Return None or handle the empty case as appropriate
    
    if year < newdata["Year"].min():
        return 0
    
    if year<=2020 :
        outcome_data = newdata.loc[newdata["Year"]==year]
        return outcome_data["CO2 emission (Tons)"]
    
    X = newdata.iloc[:, 4].values
    Y = newdata.iloc[:, 5].values
    Y = Y.reshape(-1, 1)
    
    poly_reg = PolynomialFeatures(degree=2)
    X_poly = poly_reg.fit_transform(X.reshape(-1, 1))
    
    lin_reg_poly = LinearRegression()
    lin_reg_poly.fit(X_poly, Y)
    
    outcome = lin_reg_poly.predict(poly_reg.fit_transform([[year]]))
    return outcome

def giveX(country):
    dataset = pd.read_csv('emissiondata.csv')
    newdata = dataset.loc[dataset["Code"] == country]
    return newdata["Year"].values

def giveY(country):
    dataset = pd.read_csv('emissiondata.csv')
    newdata = dataset.loc[dataset["Code"] == country]
    return newdata["CO2 emission (Tons)"].values

def giveName(country):
    dataset = pd.read_csv('emissiondata.csv')
    newdata = dataset.loc[dataset["Code"]==country]
    names = newdata["Country"].values
    return names[0]



