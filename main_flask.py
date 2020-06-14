import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from flask import Flask, render_template, request
import logging
import urllib.parse
import requests

app = Flask(__name__)

dataset = pd.read_csv("model_data.csv")
X = dataset[["co", "no2", "o3", "pm10", "so2"]]
y = dataset["pm25"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = RandomForestRegressor(n_estimators=500, max_features=2)
model.fit(X_train, y_train)


@app.route('/')
def student():
    return render_template('main_index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # city = request.form['no']
        city = format(request.form['loc'])
        main_api = 'http://api.openaq.org/v1/latest?'

        url = main_api + urllib.parse.urlencode({'city': city})
        json_data = requests.get(url).json()
        for each in json_data['results'][0]['measurements']:
            # print(each['parameter'], each['value'])
            if each['parameter'] == 'co':
                co = each['value']
            elif each['parameter'] == 'so2':
                so2 = each['value']
            elif each['parameter'] == 'pm10':
                pm10 = each['value']
            elif each['parameter'] == 'pm25':
                pm25 = each['value']
            elif each['parameter'] == 'o3':
                o3 = each['value']
            elif each['parameter'] == 'no2':
                no2 = each['value']

        print("Before")
        result = model.predict([[co, no2, o3, pm10, so2]])[0]
        app.logger.warning(result)

        if (pm25 < 12):
            val = "Good"
            return render_template("good.html", result={"result": val}, pm25=pm25)
        elif ((pm25 > 12.1) and (pm25 < 35.4)):
            val = "Moderate"
            return render_template("moderate.html", result={"result": val}, pm25=pm25)
        elif ((pm25 > 35.5) and (pm25 < 55.4)):
            val = "Unhealthy"
            return render_template("unhealthy_sens.html", result={"result": val}, pm25=pm25)
        elif ((pm25 > 55.5) and (pm25 < 150.4)):
            val = "Very Unhealthy"
            return render_template("unhealthy.html", result={"result": val}, pm25=pm25)
        elif (pm25 > 250):
            val = "Hazardous"
            return render_template("haz.html", result={"result": val}, pm25=pm25)


if __name__ == '__main__':
    app.run(debug=True)
