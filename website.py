import streamlit as st
import joblib
import pandas as pd

st.write("### Weather Prediction Website to play Cricket")

col1, col2 = st.columns(2)

OutlookNum = col1.selectbox("How is the weather?", ['Sunny', 'Overcast', 'Rainy'])

TempNum = col2.selectbox("What's the temperature", ['Hot', 'Mild', 'Cold'])

HumidityNum = col1.radio("The humidity level", ['High', 'Normal'])

WindNum = col2.radio("Is it windy?", ['Yes', 'No'])

Predictions = pd.DataFrame([[OutlookNum, TempNum, HumidityNum, WindNum]], 
columns = ['OutlookNum', 'TempNum', 'HumidityNum', 'WindNum'])

def transformWeather(data):
    output = 2
    if (data == 'Overcast'):
        output = 0
    elif(data == 'Rainy'):
        output = 1
    return(output)

def transformTemp(data):
    output = 2
    if(data == 'Cold'):
        output = 0
    elif(data == 'Hot'):
        output = 1
    return output

Predictions['OutlookNum'] = Predictions['OutlookNum'].apply(transformWeather)

Predictions['TempNum'] = Predictions['TempNum'].apply(transformTemp)

Predictions['HumidityNum'] = Predictions['HumidityNum'].apply(lambda x : 1 if x == 'Normal' else 0)

Predictions['WindNum'] = Predictions['WindNum'].apply(lambda x : 1 if x == 'Yes' else 0)

model = joblib.load('WeatherDataModel.pkl')

predicted = model.predict(Predictions)

if st.button("Predict"):
    if(predicted[0] == 'Yes'):
        st.write("### You can successfully play the cricket match!")
    else:
        st.write("### You cannot play the cricket match today.")
