from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource
from flask import (abort, current_app, jsonify,
                   make_response, request, send_file)

import csv
import pymysql
import json
import datetime

DATA_FILE = "./data.csv"

app = Flask(__name__)
CORS(app)
api = Api(app)

with open("route.json", 'r') as f:
    ROUTE = json.load(f)

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

def SQL_update(sql):
    conn = pymysql.connect(host = '182.61.17.45', 
                    user = "csc4001",
                    passwd = "123456", 
                    database = "Hospital")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

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
    fileObj.save('1.jpeg')
    #print(fileObj.read())

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
    username = data['username']
    password = data['password']

    sql = f"SELECT * from Account WHERE id = '{username}'"
    df = SQL_query(sql)

    if len(df) == 0:
        return_data = {
            'code': 60001, # unknown user
            'message': 'Unknown User'
        }
    elif df[0][0] != password:
        return_data = {
            'code': 60002, # unknown user
            'message': 'Invalid Password'
        }
    else:
        return_data = {
            "code": 20000,
            "data": {
                'token': df[0][3]
            }
        }
    # return_data = {
    #     "code": 20000,
    #     "data": {
    #         'token':"admin-token",
    #     }
    # }
    # error_return = {
    #     'code': 12345,
    #     'message': 'ERROR data'
    # }
    return make_response(jsonify(return_data))


@app.route('/api/user/info', methods=['GET','POST'])
def test2():
    data = request.get_json(silent=True)
    token = data['token'].split(',')
    return_data = {
        'code': 20000,
        'data': {
            'roles': [token],
            'introduction': f'I am a {token}',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': 'Super Admin',
            'menus': []
        }
    }

    for page in token:
        return_data['data']['menus'].append(ROUTE[page])
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
    
    #data = request.get_json(silent=True)
    radio_id = request.form.get("radio_id")

    #Fetch data
    sql = f'''select p.patient_id, p.name, p.birthDate, p.gender, a.sickness, c.status
            from CT c join Appointment a on c.app_id = a.app_id join Patient p on a.patient_id = p.patient_id
            where radio_id = {radio_id}
            order by c.status'''
    result = SQL_query(sql)
    
    for i in result:
        return_data['data'][i[0]] = {}
        return_data['data'][i[0]]["name"] = i[1]
        return_data['data'][i[0]]["birthDate"] = i[2].strftime("%Y-%m-%d")
        return_data['data'][i[0]]["gender"] = i[3]
        return_data['data'][i[0]]["sickness"] = i[4]
        return_data['data'][i[0]]["status"] = i[5]

    return make_response(jsonify(return_data))

""" @app.route('/generate_CT_report', methods=['GET','POST'])
def generate_CT_report(): """

@app.route('/upload_CT_report', methods=['GET','POST'])
def upload_CT_report():
    patient_id = request.form.get("patient_id")
    report = request.form.get("report")
    ''' 通过sql将报告存入CT '''
    SQL_update(f'''update CT c inner join Appointment a on c.app_id = a.app_id set report = "{report}", c.status = "finished" 
    where patient_id = {patient_id} and c.status = "waiting"''')
    return_data = {
        'code': 20000,
        'data': {'patient_id': patient_id}
    }
    return make_response(jsonify(return_data))


@app.route('/upload_sickness', methods=['GET','POST'])
def upload_sickness():
    patient_id = request.form.get("patient_id")
    sickness = request.form.get("sickness")
    ''' 通过sql将sickness存入Appointment '''
    SQL_update(f'''update Appointment set sickness = "{sickness}" where patient_id = {patient_id} and status = "processing"''')
    return_data = {
        'code': 20000,
        'data': {'patient_id': patient_id}
    }
    return make_response(jsonify(return_data))

@app.route('/get_main_list', methods=['GET','POST'])
def get_main_list():
    return_data = {
        'code': 20000,
        'data': {}
    }
    out_doc_id = request.form.get("out_doc_id")
    ''' 需要这个主治医师名下，appointment.status为processing的 appointment '''
    '''{'111':{'name': '', 'birthdate': '', 'gender': '', 'sickness': '', 'ct_status': '', 'report': ''},
    '222': {},
    '333': {}
    }'''
    sql = f'''select p.patient_id, p.name, p.birthDate, p.gender, a.sickness, c.status, report
            from CT c join Appointment a on c.app_id = a.app_id join Patient p on a.patient_id = p.patient_id
            where outdoc_id = {out_doc_id} and a.status = "processing"
            order by c.status  '''
    result = SQL_query(sql)

    for i in result:
        return_data['data'][i[0]] = {}
        return_data['data'][i[0]]["name"] = i[1]
        return_data['data'][i[0]]["birthDate"] = i[2]
        return_data['data'][i[0]]["gender"] = i[3]
        return_data['data'][i[0]]["sickness"] = i[4]
        return_data['data'][i[0]]["ct_status"] = i[5]
        return_data['data'][i[0]]["report"] = i[6]
    return make_response(jsonify(return_data))

#'radio_id直接特殊定一个吧: 定为1'
@app.route('/arrange_CT', methods=['GET','POST'])
def arrange_CT():
    return_data = {
        'code': 20000,
        'data': {}
    }
    patient_id = request.form.get("patient_id")
    
    result = SQL_query(f'''select count(*) from CT c join Appointment a on c.app_id = a.app_id 
    where patient_id = {patient_id} and c.status = "waiting"''')
    if result[0][0]!=0:
        return_data = {
            'code': 00000,
            'message': "Error: cannot create a new CT order when the previous one has not finished"
        }
    else:
        # find CT_id for the new CT
        # if there is no CT created before, make this the first one.
        result = SQL_query('select max(CT_id) from CT')
        if type(result[0][0])!=int:
            CT_id = 1
        else:
            CT_id = result[0][0]+1
        # find the app_id
        result = SQL_query(f'''select app_id 
        from Appointment a join Patient p on a.patient_id = p.patient_id 
        where a.patient_id = {patient_id} and status = "processing"''')
        if len(result)==0:
            return_data = {
                'code': 00000,
                'message': "Error: no processing appointment for this patient"
            }
        else:
            app_id = result[0][0]
            sql = f'''insert into CT values({CT_id},{app_id}, 1, "", "", "waiting")'''
            SQL_update(sql)

    return make_response(jsonify(return_data))

''' 在appoingment里把status改为finished '''
@app.route('/finish_appointment', methods=['GET','POST'])
def finish_appointment():
    patient_id = request.form.get("patient_id")
    sql = f'''update Appointment a inner join Patient p on a.patient_id = p.patient_id set status = "finished" 
    where status = "processing" and p.patient_id = {patient_id}'''
    SQL_update(sql)

    return_data = {
        'code': 20000,
        'data': {'patient_id': patient_id}
    }
    return make_response(jsonify(return_data))

@app.route('/get_CT_doctor_profile', methods=['GET','POST'])
def get_CT_doctor_profile():
    return_data = {
        'code': 20000,
        'data': {}
    }
    doc_id = request.form.get("doc_id")
    ''' {'name': '', 'doc_id': '', 'gender': '', 'phone': '', 'department': '', 'office': '', 'title': '', 'specialty': ''} '''
    result = SQL_query(f'''select * from Radiologist where radio_id = {doc_id}''')

    if (len(result)==0):
        return_data = {
            'code': 00000,
            'message': 'Cannot find the radiologist'
        }
    else:
        return_data['data']['name'] = result[0][1]
        return_data['data']['doc_id'] = result[0][0]
        return_data['data']['gender'] = result[0][2]
        return_data['data']['phone'] = result[0][3]
        return_data['data']['department'] = result[0][4]
        return_data['data']['office'] = result[0][5]
        return_data['data']['title'] = result[0][6]
        return_data['data']['specialty'] = result[0][7]

    return make_response(jsonify(return_data))


@app.route('/get_main_doctor_profile', methods=['GET','POST'])
def get_main_doctor_profile():
    return_data = {
        'code': 20000,
        'data': {}
    }
    doc_id = request.form.get("doc_id")
    ''' {'name': '', 'doc_id': '', 'gender': '', 'phone': '', 'department': '', 'office': '', 'title': '', 'specialty': ''} '''

    result = SQL_query(f'''select * from Out_doctor where outdoc_id = {doc_id}''')
    if len(result)==0:
        return_data = {
            'code': 00000,
            'message': 'Cannot find the outpatient doctor'
        }
    else:
        return_data['data']['name'] = result[0][1]
        return_data['data']['doc_id'] = result[0][0]
        return_data['data']['gender'] = result[0][2]
        return_data['data']['phone'] = result[0][3]
        return_data['data']['department'] = result[0][4]
        return_data['data']['office'] = result[0][5]
        return_data['data']['title'] = result[0][6]
        return_data['data']['specialty'] = result[0][7]

    return make_response(jsonify(return_data))

@app.route('/get_patient_dashboard', methods=['GET','POST'])
def get_patient_dashboard():
    return_data = {
        'code': 20000,
        'data': {}
    }
    patient_id = request.form.get("patient_id")
    ''' 有几个人在CT表中先于这个人，等待时间为5*前面的人数 '''
    ''' {'name': '', 'people': '', 'time': ''}'''
    #find the patient's CT_id
    sql = f'''select name, CT_id from CT c join Appointment a on c.app_id = a.app_id join Patient where a.patient_id = {patient_id} and c.status = "waiting"'''
    result = SQL_query(sql)
    if len(result)==0:
        return_data = {
            'code': 00000,
            'message': "Cannot find the patient's CT order"
        }
    else:
        name = result[0][0]
        CT_id = result[0][1]
        sql = f'''select count(CT_id) from CT where CT_id < {CT_id} and status = "waiting"'''
        result = SQL_query(sql)
        return_data['data']['name'] = name
        return_data['data']['people'] = result[0][0]
        return_data['data']['time'] = result[0][0]*5
    return make_response(jsonify(return_data))


@app.route('/get_doc_dashboard', methods=['GET','POST'])
def get_doc_dashboard():
    return_data = {
        'code': 20000,
        'data': {}
    }
    doc_id = request.form.get("doc_id")
    ''' 有几个人在appointment里是processing
        有几个人在ct里是waiting
        有几个人在appointment里是finished
        appointment里总共几个人 '''
    ''' {'name': '', 'processing': '', 'waiting': '', 'finished': '', 'total': ''}'''
    # get name and total
    sql = f'''select name, count(app_id) from Out_doctor o join Appointment a on o.outdoc_id = a.outdoc_id where o.outdoc_id = {doc_id}'''
    result = SQL_query(sql)
    name = result[0][0]
    total = result[0][1]
    # get processing
    sql = f'''select count(*) from Appointment where outdoc_id = {doc_id} and status = "processing"'''
    result = SQL_query(sql)
    processing = result[0][0]
    # get finished
    sql = f'''select count(*) from Appointment where outdoc_id = {doc_id} and status = "finished"'''
    result = SQL_query(sql)
    finished = result[0][0]
    # get waiting
    sql = f'''select count(*) from Appointment a join CT c on a.app_id = c.app_id where c.status = "waiting" '''
    result = SQL_query(sql)
    waiting = result[0][0]

    return_data['data']['name'] = name
    return_data['data']['processing'] = processing
    return_data['data']['waiting'] = waiting
    return_data['data']['finished'] = finished
    return_data['data']['total'] = total

    return make_response(jsonify(return_data))

@app.route('/update_privilege', methods=['GET','POST'])
def update_privilege():
    return_data = {
        'code': 20000,
        'data': {}
    }
    data = request.get_json(silent=True)
    id_ = data['id']
    privilege = data['privilege']
    sql = f'''update Account set privilege = "{privilege}" where id = {id_}'''
    SQL_update(sql)
    return make_response(jsonify(return_data))

@app.route('/get_user_list', methods=['GET','POST'])
def get_user_list():
    return_data = {
        'code': 20000,
        'data': []
    }
    #{0: {'role': "", 'privilege': ""} ,
    # 1: {'role': "", 'privilege': ""} ,
    # 2: {'role': "", 'privilege': ""} ,}
    sql = f'''select id, identity, privilege from Account'''
    result = SQL_query(sql)
    for i in result:
        return_data['data'].append({
            'id': i[0],
            'name': 'doctor',
            'roles': i[1],
            'privilege': i[2].split(','),
            'unchange': True
        })
        # return_data['data'][i[0]] = {}
        # return_data['data'][i[0]]['role'] = i[1]
        # return_data['data'][i[0]]['privilege'] = i[2]
    return make_response(jsonify(return_data))

@app.route('/get_appointment_list', methods=['GET','POST'])
def get_appointment_list():
    return_data = {
        'code': 20000,
        'data': {}
    }
    #{0: {'role': "", 'privilege': ""} ,
    # 1: {'role': "", 'privilege': ""} ,
    # 2: {'role': "", 'privilege': ""} ,}
    sql = f'''select outdoc_id, name, gender, department, office, title, specialty, outdoc_status from Out_doctor order by outdoc_status'''
    result = SQL_query(sql)
    for i in result:
        return_data['data'][i[0]] = {}
        return_data['data'][i[0]]['name'] = i[1]
        return_data['data'][i[0]]['gender'] = i[2]
        return_data['data'][i[0]]['department'] = i[3]
        return_data['data'][i[0]]['office'] = i[4]
        return_data['data'][i[0]]['title'] = i[5]
        return_data['data'][i[0]]['specialty'] = i[6]
        return_data['data'][i[0]]['status'] = i[7]
    return make_response(jsonify(return_data))

@app.route('/arrange_appointment', methods=['GET','POST'])
def arrange_appointment():
    return_data = {
        'code': 20000,
        'data': {}
    }
    patient_id = request.form.get("patient_id")
    outdoc_id = request.form.get("outdoc_id")

    #check whether there is a processing appointment for the patient
    sql = f'''select count(*) from Appointment where patient_id = {patient_id} and status = "processing"'''
    result = SQL_query(sql)
    if result[0][0] != 0:
        return_data = {
            'code': 00000,
            'message': "You are currently in a processing appointment. You may not make a new one before the current one finishes"
        }
    else:
        # {'app_id': , 'waiting': }
        # find the app_id for the new appointment
        # if there is no CT created before, make this the first one.
        result = SQL_query('select max(app_id) from appointment')
        app_id = 1
        if type(result[0][0])!=int:
            pass
        else:
            app_id = result[0][0]+1

        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = f'''insert into Appointment values({app_id},{patient_id},{outdoc_id},"{time}","","","","","processing")'''
        SQL_update(sql)

        # return the app_id and the number of appointment he has to wait
        sql = f'''select count(*) from Appointment where outdoc_id = {outdoc_id} and status = "processing"'''
        result = SQL_query(sql)
        waiting = result[0][0] - 1
        return_data['data']['app_id'] = app_id
        return_data['data']['waiting'] = waiting

    return make_response(jsonify(return_data))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
