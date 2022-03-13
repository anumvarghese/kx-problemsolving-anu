"""
Storage service 
Module used to read and store data 

"""

#import redis
import json
import os

from flask import Flask
from flask import Flask, request, jsonify


app = Flask(__name__)


redis_host = "localhost"
redis_port = 6379
redis_password = ""



@app.route("/")
def index_page():
    """
    Index page
    """ 
    return ("Hello from storage.")    

def write_json(file_name, data):
    """
    :param: file_name: input file name
    :param: data input data
    :return 
    """
    with open(file_name, "w") as outfile:
        json.dump(data, outfile)

def read_json(file_name):
    """
    # Reading from json file
    :param: file_name: input file name
    :return json data
    """
    
    with open(file_name, 'r') as openfile:
        json_object = json.load(openfile)
    
    return json_object
    
@app.route('/store-data', methods=['POST']) 
def store_data():
    """
    Store data in memory
    Used redis to store data and commented the code since it is not working 
    Data stored temporary in File 
    """
    try:
        data_dict = {}       
        data = request.json
        name =  data.get("name")
        
        #Commenting redis code as it having some issue with docker
        #redis_obj = redis.Redis()        
        #data = json.dumps(data)
        #redis_obj.set(name, data)

        data_dict[name] = data
        file_name = "dummy.json"

        #Saving data in file
        write_json(file_name, data_dict)
        
        message = "Success"
        status_code = 200
    except Exception as e:
        message = "Failure"
        status_code = 500

    return json.dumps({'message': message}), status_code, {'ContentType':'application/json'}


@app.route('/read-data', methods=['GET']) 
def read_data():
    """
    Read data from gateways service
    :params: name
    """
    try:        
        name = request.args.get('name')
        
        #Commenting redis code as it having some issue with docker
        #redis_obj = redis.Redis()
        #data = redis_obj.get(name)
        #data = json.loads(data) 

        file_name = "dummy.json"
        #Read data from json file
        resp_data = read_json(file_name)
        data = resp_data.get(name)

    except Exception as e:
        data = e

    return jsonify(data)


if __name__ == "__main__":
    """
    Main  
    """
    app.run(host="0.0.0.0", debug=True)
    #app.run(
    #    host=os.environ.get("BACKEND_HOST", "172.0.0.1"),
    #    #port=your_port,
    #    debug=True,
    #)
