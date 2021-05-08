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

def SQL_query(sql):
    conn = pymysql.connect(host = '182.61.17.45', 
                    user = "csc4001",
                    passwd = "123456", 
                    database = "Hospital")
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

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


''' input: radio_id '''
''' {'111':{'name': '', 'birthdate': '', },
    '222': {},
    '333': {}
    }'''
@app.route('/get_CT_list', methods=['GET','POST'])
def get_CT_list():

    return_data= {
        'code' : 20000,
        'data' : {}
    }
    
    data = request.get_json(silent=True)
    radio_id = data['radio_id']

    #Fetch data
    sql = f'''select p.patient_id, p.name, p.birthDate, p.gender, a.sickness, c.status
            from CT c join Appointment a on c.app_id = a.app_id join Patient p on a.patient_id = p.patient_id
            where radio_id = {radio_id}
            order by c.status'''
    result = SQL_query(sql)
    
    for i in result:
        return_data['data'][i[0]] = {}
        return_data['data'][i[0]]["name"] = i[1]
        return_data['data'][i[0]]["birthDate"] = i[2]
        return_data['data'][i[0]]["gender"] = i[3]
        return_data['data'][i[0]]["sickness"] = i[4]
        return_data['data'][i[0]]["status"] = i[5]

    return make_response(jsonify(return_data))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
