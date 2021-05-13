import pymysql
import datetime
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

def get_CT_list(radio_id):

    return_data= {
        'code' : 20000,
        'data' : {}
    }
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

    return return_data

def upload_CT_report(patient_id,report):
    ''' 通过sql将报告存入CT '''
    SQL_update(f'''update CT c inner join Appointment a on c.app_id = a.app_id set report = "{report}", c.status = "finished" 
    where patient_id = {patient_id} and c.status = "waiting"''')
    return_data = {
        'code': 20000,
        'data': {'patient_id': patient_id}
    }
    return return_data

def arrange_CT(patient_id):
    return_data = {
        'code': 20000,
        'data': {}
    }
    
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

    return return_data

def finish_appointment(patient_id):
    sql = f'''update Appointment a inner join Patient p on a.patient_id = p.patient_id set status = "finished" 
    where status = "processing" and p.patient_id = {patient_id}'''
    SQL_update(sql)

    return_data = {
        'code': 20000,
        'data': {'patient_id': patient_id}
    }
    return return_data

def get_main_list(out_doc_id):
    return_data = {
        'code': 20000,
        'data': {}
    }
    sql = f'''select p.patient_id, p.name, p.birthDate, p.gender, a.sickness, c.status, report
            from CT c join Appointment a on c.app_id = a.app_id join Patient p on a.patient_id = p.patient_id
            where outdoc_id = {out_doc_id} and a.status = "processing"
            order by c.status  '''
    result = SQL_query(sql)
    if len(result) != 0:
        for i in result:
            return_data['data'][i[0]] = {}
            return_data['data'][i[0]]["name"] = i[1]
            return_data['data'][i[0]]["birthDate"] = i[2]
            return_data['data'][i[0]]["gender"] = i[3]
            return_data['data'][i[0]]["sickness"] = i[4]
            return_data['data'][i[0]]["ct_status"] = i[5]
            return_data['data'][i[0]]["report"] = i[6]
    else:
        return_data = {
            'code': 00000,
            'message': 'Cannot find the doctor'
        }
    return return_data

print(get_main_list(2))
print(get_main_list(0))



def update_privilege(id_, privilege):
    return_data = {
        'code': 20000,
        'data': {}
    }

    sql = f'''update Account set privilege = "{privilege}" where id = {id_}'''
    SQL_update(sql)
    return return_data

def get_user_list():
    return_data = {
        'code': 20000,
        'data': {}
    }
    #{0: {'role': "", 'privilege': ""} ,
    # 1: {'role': "", 'privilege': ""} ,
    # 2: {'role': "", 'privilege': ""} ,}
    sql = f'''select id, identity, privilege from Account'''
    result = SQL_query(sql)
    for i in result:
        return_data['data'][i[0]] = {}
        return_data['data'][i[0]]['role'] = i[1]
        return_data['data'][i[0]]['privilege'] = i[2]
    return return_data

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
    return return_data

def arrange_appointment(patient_id,outdoc_id):
    return_data = {
        'code': 20000,
        'data': {}
    }

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
        result = SQL_query('select max(app_id) from Appointment')
        app_id = 1
        if type(result[0][0])!=int:
            pass
        else:
            app_id = result[0][0]+1
        print(app_id)
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = f'''insert into Appointment values({app_id},{patient_id},{outdoc_id},"{time}","","","","","processing")'''
        SQL_update(sql)

        # return the app_id and the number of appointment he has to wait
        sql = f'''select count(*) from Appointment where outdoc_id = {outdoc_id} and status = "processing"'''
        result = SQL_query(sql)
        waiting = result[0][0] - 1
        return_data['data']['app_id'] = app_id
        return_data['data']['waiting'] = waiting

    return return_data

def get_patient_dashboard2(patient_id):
    return_data = {
        'code': 20000,
        'data': {}
    }
    ''' 有几个人挂他的医生的号在他前面，等待时间为10*前面的人数 '''
    ''' {'name': '', 'people': '', 'time': ''}'''
    #find the patient's name
    result = SQL_query(f'''select name from Patient where patient_id = {patient_id}''')
    name = result[0][0]
    #find the patient's doctor and his app_id
    sql = f'''select app_id, outdoc_id from Appointment where patient_id = {patient_id} and status = "processing"'''
    result = SQL_query(sql)
    if len(result) == 0:
        return_data['data']['name'] = name
        return_data['data']['people'] = ""
        return_data['data']['time'] = ""
    else:
        app_id = result[0][0]
        outdoc_id = result[0][1]
        sql = f'''select count(*) from Appointment where outdoc_id = {outdoc_id} and app_id <{app_id} and status = "processing"'''
        result = SQL_query(sql)
        people = result[0][0]
        return_data['data']['name'] = name
        return_data['data']['people'] = people
        return_data['data']['time'] = people*5
    return return_data

def get_patient_dashboard(patient_id):
    return_data = {
        'code': 20000,
        'data': {}
    }
    ''' 有几个人在CT表中先于这个人，等待时间为5*前面的人数 '''
    ''' {'name': '', 'people': '', 'time': ''}'''
    #find the patient's name
    result = SQL_query(f'''select name from Patient where patient_id = {patient_id}''')
    name = result[0][0]
    #find the patient's CT_id
    sql = f'''select CT_id from CT c join Appointment a on c.app_id = a.app_id join Patient where a.patient_id = {patient_id} and c.status = "waiting"'''
    result = SQL_query(sql)
    if len(result)==0:
        return_data['data']['name'] = name
        return_data['data']['people'] = ""
        return_data['data']['time'] = ""
    else:
        name = result[0][0]
        CT_id = result[0][1]
        sql = f'''select count(CT_id) from CT where CT_id < {CT_id} and status = "waiting"'''
        result = SQL_query(sql)
        return_data['data']['name'] = name
        return_data['data']['people'] = result[0][0]
        return_data['data']['time'] = result[0][0]*5
    return return_data

result = SQL_query(f'''select * 
    from Appointment; alter table Account add test varchar(45)''')
print(result)

#print(upload_CT_report(3,""))
#print(arrange_CT(3))


#print(finish_appointment(3))

#print(update_privilege(0, 'dash,role_management'))
#print(get_user_list())

#print(get_CT_list(1))

#print(get_appointment_list())
#print(finish_appointment(3))
#print(arrange_appointment(3,2))

#print(get_patient_dashboard2(3))
#print(get_patient_dashboard(3))