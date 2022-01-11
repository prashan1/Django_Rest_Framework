import requests, json
# url='http://127.0.0.1:8000/students'
# response = requests.get(url).json()
# print(response)
# url='http://127.0.0.1:8000/create-student/'
# request = {"name":'Rakesh Tyagi','age':20,'rollno':333}
# # json_data = json.dumps(request)
# # response = requests.post(url=url, data=json_data)
# # print(response.json())

def get_data(id=None):
    URL='http://127.0.0.1:8000/show-student/'   
    data = {'id':id}
    json_data = json.dumps(data)
    response = requests.get(url=URL, data = json_data)
    print(response.json())


def create_data():
    URL='http://127.0.0.1:8000/create-student/'   
    request = {"name":'Pankaj Mularar','age':1,'rollno':3323}
    json_data = json.dumps(request)
    response = requests.post(url=URL, data=json_data)
    print(response.json())

# create_data()


def udpate_data():
    URL='http://127.0.0.1:8000/udpate-student/'   
    request = {"id":11 , "name":'Tony Stark'}
    json_data = json.dumps(request)
    response = requests.put(url=URL, data=json_data)
    print(response.json())

# udpate_data()



def delete_data():
    URL='http://127.0.0.1:8000/delete-student/'   
    request = {"id":100 }
    json_data = json.dumps(request)
    response = requests.delete(url=URL, data=json_data)
    print(response.json())

# delete_data()
get_data()