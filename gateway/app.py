"""
Gateway service
"""
#import redis
import requests
import json
import os
import docker

from flask import Flask, render_template
from flask import Flask, request, jsonify


app = Flask(__name__, template_folder='templates')
storage_url = 'http://storage:8081'
RUNNING = 'running'


@app.route("/")
def index_page():
    """
    Index page
    """ 
    return render_template('index.html')

def get_storage_status(storage_url):
    resp = requests.get(storage_url)
    return resp


def container_status(image_name):
    """
    Check the container Image is running
    
    verify the status of a sniffer container by it's name
    :param image_name: the Image name of the container
    :return: Boolean if the status is ok
    """
    client = docker.from_env()
    containers = client.containers.list()
    container_is_running = False
    for container in containers:
        if 'storage' in container.attrs.get('Name'):
            container_state = container.attrs['State']
            container_is_running = container_state['Status'] == RUNNING
    
    return container_is_running


@app.route('/sstatus')
def sstatus():
    """
    Stroge service  status
    """
    try:
        cimage_name = "storage"
        message = get_storage_status(storage_url)
        #message = "Success" if container_status(cimage_name) else "Failure"
        status_code = 200         
    except Exception as e:
        status_code = 500
        message = str(e)
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
            message = str(e)
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
            message = str(e)
            status_code = 404
            
        return jsonify(message=message,
                    statusCode= status_code), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
    #app.run(
    #    host=os.environ.get("BACKEND_HOST", "172.0.0.1"),
    #    #port=your_port,
    #    debug=True,
    #)
