"""
Gateway service
"""
#import redis
import requests
import json
import os

from flask import Flask, render_template
from flask import Flask, request, jsonify


app = Flask(__name__, template_folder='templates')
storage_url = 'http://localhost:8081/'


@app.route("/")
def index_page():
    """
    Index page
    """ 
    return render_template('index.html')


@app.route("/stats")
def gateway_status():
    """
    Gateway status
    """
    try:
        response = requests.get(storage_url)
        message = "Success"
        status_code = response.status_code 
    except Exception as e:
        status_code = 500
        message = e


    return jsonify(message= message,
                   statusCode= status_code), status_code


@app.route('/data', methods=['GET', 'POST']) 
def process_data():
    """
    Functionlity to read and wrtie dummy data and store in redis memory
    """
    #Handle get request
    if request.method == 'GET':
        try:
            name = request.args.get('name')
            payload = {'name': name}
            read_url = "/".join([storage_url, 'read-data'])
            response = requests.get(read_url, params=payload)
            message = "Success"
            data = response.json()
            status_code = response.status_code
        except Exception as e:
            message = e
            data = ""
            status_code = 404

        return jsonify(message= message,
                    statusCode= status_code,
                    data= data), status_code

    #Handle post request 
    elif request.method == 'POST':
        try:
            store_data_url = "/".join([storage_url, "store-data"])
            
            raw_data = request.json
            response = requests.post(url=store_data_url, json=raw_data)
            status_code = response.status_code 
            message = "Success"
        except Exception as e:
            message = e
            status_code = 404
            
        return jsonify(message=message,
                    statusCode= status_code), status_code


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8085)
