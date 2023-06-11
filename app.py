import sys
import os

from flask import Flask, request, render_template, url_for,redirect

from src.components import data_ingestion
from src.components import data_transformation
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException
from src.logger import logging


import pickle
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

app= Flask(__name__)

# route for home page
@app.route('/')
def index():
    return render_template('kartik/index.html')

@app.route('/mlmodel')
def mlmodel():
    return render_template('home.html')


@app.route('/predictdata', methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        cropa_area = request.form.get('cropa_area')
        cropb_area = request.form.get('cropb_area')
        cropc_area = request.form.get('cropc_area')
        cropd_area = request.form.get('cropd_area')
        crope_area = request.form.get('crope_area')
        print(cropa_area, cropb_area, latitude, longitude, crope_area)

        data = CustomData(lat=float(latitude),
                           long=float(longitude),
                           cropa_area = float(cropa_area),
                           cropb_area = float(cropb_area),
                           cropc_area = float(cropc_area),
                           cropd_area = float(cropd_area),
                           crope_area = float(crope_area)
                           )
        
        logging.info('dataframe is being created')

    pred_df = data.get_data_as_data_frame()
    print(pred_df)

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    return render_template('home.html', results = abs(results[0]))



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)


