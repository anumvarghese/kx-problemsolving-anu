"""
"""
import requests
import json



class ServiceAssembly():
    def __init__(self):
        self.data_gt_url = 'http://localhost:8085/data'
        self.status_url = 'http://localhost:8085/sstatus'

    def read_data(self):
        """
        Function to read data 
        """
        print ("read data ")
        payload = {'name': 'Noel'}
        resp = requests.get(self.data_gt_url, params=payload)
        print (resp.text)  
        return resp


    def write_data(self):
        """
        Function to write data
        """
        create_row_data = {'id': '1235','name':'Noel','created_on':'27/01/2018','modified_on':'27/01/2018','desc':'This is Noel !!'}
        resp = requests.post(url=self.data_gt_url, json=create_row_data)
        print(resp.status_code, resp.reason, resp.text)
        return resp

    def status_check(self):
        """
        Storage status check
        """
        resp = requests.get(self.status_url)
        print (resp.text)
        return resp



if __name__ == "__main__":
    sa_obj = ServiceAssembly()
    while True:
        print (" 1. Status Check ")
        print (" 2. Write data ")
        print (" 3. Read data ")
        print (" 4. Exit ")
        choice = input("Enter the choice :")
        print ("choice ", choice)
        if choice == '4':
            break
        elif choice == '1':
            resp = sa_obj.status_check()
            print (resp)
        elif choice == '2':
            resp = sa_obj.write_data()
            print (resp)
        elif choice == '3':	
            resp = sa_obj.read_data()
            print (resp)

