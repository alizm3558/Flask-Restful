# -*- coding:utf-8 -*-
from flask import Flask, render_template, make_response, jsonify, request, url_for
from flask_restful import Resource, Api

from helpers.DataHelpers import DataHelpers

app = Flask(__name__)
api = Api(app)
app.config['JSON_AS_ASCII'] = False # türkçe karakter desteği sağladı

class catchpoint_test_details(Resource):
    def get(self):  # post ile veri alıyoruz, çalışıyor
        data_helpers = DataHelpers()
        return jsonify(data_helpers.all_select())



api.add_resource(catchpoint_test_details, '/allSelect')

if __name__ == "__main__":
    app.run(debug=True)