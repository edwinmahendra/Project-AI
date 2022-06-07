from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
# import pandas as pd
# import ast
import main

app = Flask(__name__)
app.config["BUNDLE_ERRORS"] = True
api = Api(app)

class Conclude(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        # parser.add_argument('test', required=True)  # add args
        # argu = parser.parse_args()  # parse arguments to dictionary
        # # print(argu)
        # return {'aha':'aha'}

        
        parser.add_argument('kepadatan_penduduk', required=True)  # add args
        parser.add_argument('daerah_sungai', required=True)
        parser.add_argument('kemiringan_lereng', required=True)
        parser.add_argument('ketinggian_wilayah', required=True)
        parser.add_argument('curah_hujan', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        hasil = main.getResult(args['kepadatan_penduduk'], args['daerah_sungai'], args['kemiringan_lereng'], args['ketinggian_wilayah'], args['curah_hujan'])
        return hasil
        
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        # parser.add_argument('test', required=True)  # add args
        # argu = parser.parse_args()  # parse arguments to dictionary
        # # print(argu)
        # return {'aha':'aha'}

        
        parser.add_argument('kepadatan_penduduk', required=True)  # add args
        parser.add_argument('daerah_sungai', required=True)
        parser.add_argument('kemiringan_lereng', required=True)
        parser.add_argument('ketinggian_wilayah', required=True)
        parser.add_argument('curah_hujan', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        hasil = main.getResult(args['kepadatan_penduduk'], args['daerah_sungai'], args['kemiringan_lereng'], args['ketinggian_wilayah'], args['curah_hujan'])
        return hasil

api.add_resource(Conclude, '/conclude')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
