from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource
from flask import (abort, current_app, jsonify,
                   make_response, request, send_file)

import csv
import pymysql
DATA_FILE = "./data.csv"

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/', methods=["GET"])
def index():
    return "Welcome to API v1, try /hello."

@app.route('/test', methods=['GET','POST'])
def test():
    return_data = {
        "code": 20000,
        "data": "admin-token",
    }
    return make_response(jsonify(return_data))

@app.route('/upload_image', methods=['GET','POST'])
def upload_image():
    name = request.form.get("name")
    description = request.form.get("description")
    fileObj = request.files.get("file")
    print(name)
    print(description)
    print(fileObj)
    print(fileObj.read())

    return_data = {
        "code": 20000,
        "data": {
            'role': "admin-token",
        }
    }
    return make_response(jsonify(return_data))

# class Hello(Resource):
#     @staticmethod
#     def get():
#         return "[get] hello flask"

#     @staticmethod
#     def post():
#         return "[post] hello flask"

# api.add_resource(Hello, '/hello')


@app.route('/api/user/login', methods=['GET','POST'])
def login_test():
    data = request.get_json(silent=True)
    return_data = {
        "code": 20000,
        "data": {
            'token':"admin-token",
        }
    }
    error_return = {
        'code': 12345,
        'message': 'ERROR data'
    }
    return make_response(jsonify(return_data))

@app.route('/api/user/info', methods=['GET','POST'])
def test2():
    data = request.get_json(silent=True)
    print(data)
    return_data = {
        'code': 20000,
        'data': {
            'roles': ['admin'],
            'introduction': 'I am a super administrator',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': 'Super Admin'
        }
    }
    return make_response(jsonify(return_data))

@app.route('/api/user/logout', methods=['GET','POST'])
def test3():
    data = request.get_json(silent=True)
    return_data = {
        'code': 20000,
        'data': 'success'
    }
    return make_response(jsonify(return_data))


@app.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    print(username, password)
    return_data = get_login(username, password)
    return make_response(jsonify(return_data))

def get_login(username, password):
    return_data = {
        'status': False,
        'id': 0,
        'role': ""
    }

    # SQL
    conn = pymysql.connect(host = '182.61.17.45', 
                       user = "csc4001",
                       passwd = "123456", 
                       database = "Hospital")
    cur = conn.cursor()

    cur.execute('select id, identity from Account where account = "%s" and password = "%s"'%(username, password))
    result = cur.fetchall()
    if (len(result) == 1):
        return_data['status'] = True
        return_data['id'] = result[0][0]
        return_data['role'] = result[0][1]

    cur.close()
    conn.close()
    return return_data

@app.route('/hello_api', methods = ['GET', 'POST'])
def hellp_api():
    data = request.get_json(silent=True)
    data_in = data['input']
    return_data = {
        'hello': "hello flask, hello vue " + data_in,
        "flask": 2
    }
    return make_response(jsonify(return_data))

@app.route('/get_released_task', methods = ['GET', 'POST'])
def get_released_task():
    data = request.get_json(silent=True)
    user_id = data['user_id']
    return_data = get_released_task_data(user_id)
    return make_response(jsonify(return_data))

def get_released_task_data(user_id):
    return_data = {
        "data": []
    }
    with open(DATA_FILE) as f:
        reader = csv.reader(f)
        head_row=next(reader)
        for row in reader:
            if row[5] == user_id:
                activity = {
                    'title': row[1],
                    'position': row[3],
                    'status': row[7],
                    'participant': row[6],
                    'key_word': row[8]
                }
                return_data['data'].append(activity)
    return return_data

@app.route('/get_participated_task', methods = ['GET', 'POST'])
def get_participated_task():
    data = request.get_json(silent=True)
    user_id = data['user_id']
    return_data = get_participated_task_data(user_id)
    return make_response(jsonify(return_data))

def get_participated_task_data(user_id):
    return_data = {
        "data": []
    }
    with open(DATA_FILE) as f:
        reader = csv.reader(f)
        head_row=next(reader)
        for row in reader:
            if row[5] != user_id:
                activity = {
                    'title': row[1],
                    'position': row[3],
                    'status': row[7],
                    'participant': row[6],
                    'key_word': row[8]
                }
                return_data['data'].append(activity)
    return return_data

@app.route('/get_task_on_map', methods = ['GET', "POST"])
def get_task_on_map():
    data = request.get_json(silent=True)
    user_id = data['user_id']
    return_data = get_map_data(user_id)
    return make_response(jsonify(return_data))

def get_map_data(user_id):
    return_data = {
        'freeData': [],
        'discountsData': []
    }
    with open(DATA_FILE) as f:
        reader = csv.reader(f)
        head_row=next(reader)
        for row in reader:
            activity = {
                'name': row[1],
                'value': [
                    float(row[4].split(',')[0][1:]), # 经度
                    float(row[4].split(',')[1][:-1]), # 纬度
                    row[3], # position
                    row[2], # distription
                    row[9], # requirement
                    row[8], # key word
                    row[11], # pic
                    row[12], # store distription
                    row[10], # task
                ]
            }
            if row[5] == user_id:
                return_data['discountsData'].append(activity)
            else:
                return_data['freeData'].append(activity) 
    return return_data

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
