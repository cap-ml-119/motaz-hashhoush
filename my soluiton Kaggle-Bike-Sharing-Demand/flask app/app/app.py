from flask import Flask, request, jsonify
from werkzeug.wrappers import Response
from io import StringIO
import numpy as np
import pandas as pd
from app import services as sv

import pickle


app = Flask(__name__)

# loding the objects
model = pickle.load(open('./modles/modle.sav', 'rb'))
scaler = pickle.load(open('./modles/scaler.sav', 'rb'))
polynomial = pickle.load(open('./modles/polynomial.sav', 'rb'))


@app.route('/api/v1/single/prediction', methods=['POST'])
def single_prediction():
    """function to predict of single sample,
        it take data as an json format

    Returns:
        [response]: [contain the predict value]
    """

    try:
        data = request.get_json()
        sv.check_required_features(data)
        data = np.array([sv.get_data_of_features(data)])

        data = scaler.fit_transform(data)
        data = polynomial.fit_transform(data)

        response = {
            "status": 200,
            "prediction of value": model.predict(data)[0][0],
        }
    except Exception as e:

        response = {
            "status": 400,
            "response": str(e)
        }

    return jsonify(response)


@app.route('/api/v1/batch/preduction', methods=['POST'])
def batch_preduction():
    """function to prediction of samples,
        it take data in file as .csv format

    Returns:
        [Response]: [file contains predictions values]
        [response]: [response as json if there any excption error]
    """
    try:
        file = request.files.get('file')
        df = pd.read_csv(StringIO(file.stream.read().decode('utf-8')))

        data = scaler.fit_transform(df)
        data = polynomial.fit_transform(data)

        preductions = model.predict(data)
        response_file_content = ''.join(
            [str(preduct[0]) + '\n' for preduct in preductions])

        return Response(response_file_content, mimetype='text/csv', headers={
            "Content-disposition": "attachment; filename=preduct.csv"
        })

    except Exception as e:
        response = {
            "status": 400,
            "response": str(e)
        }
    return jsonify(response)


def create_app():
    """function to return Flask object

    Returns:
        [app]: [Flask object created]
    """
    return app
