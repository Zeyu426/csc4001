import pymysql
from faker import Faker
import datetime
import random

conn = pymysql.connect(host = '182.61.17.45', 
                       user = "csc4001",
                       passwd = "123456", 
                       database = "Hospital")
cur = conn.cursor()

app_id = 2
CT_id = 2
fake = Faker()
sicknesses = ["Vomit","Hard to breathe","Hemoptysis","Fever","Cough","Chest pain"]
exams = ["lung CT", ""]
treatments = ['medicine','surgery']

cur.execute('select patient_id from Patient')
patients = cur.fetchall()

cur.execute('select outdoc_id from Out_doctor')
doctors = cur.fetchall()

cur.execute('select radio_id from Radiologist')
radios = cur.fetchall()


#finished appointments
'''for i in range(10):
    patient_id = random.choice(patients)[0]
    outdoc_id = 2
    time = fake.date_time_this_month().strftime("%Y-%m-%d %H:%M:%S")
    sickness_list = random.sample(sicknesses, random.randint(0,6))
    sickness = ", ".join(sickness_list)
    examination = "lung CT"
    diagnosis = "Some disease"
    treatment = random.choice(treatments)
    status = "finished"
    cur.execute('insert into Appointment values(%d,%d,%d,"%s","%s","%s","%s","%s","%s")'%(app_id,patient_id,outdoc_id,time,sickness,examination,diagnosis,treatment,status))
    app_id = app_id+1
    print(app_id)'''

#processing appointments
for i in range(10):
    patient_id = random.choice(patients)[0]
    outdoc_id = 2
    time = fake.date_time_this_month().strftime("%Y-%m-%d %H:%M:%S")
    sickness_list = random.sample(sicknesses, random.randint(1,6))
    sickness = ", ".join(sickness_list)
    examination = "lung CT"
    diagnosis = ""
    treatment = ""
    status = "processing"
    cur.execute('insert into Appointment values(%d,%d,%d,"%s","%s","%s","%s","%s","%s")'%(app_id,patient_id,outdoc_id,time,sickness,examination,diagnosis,treatment,status))
    app_id = app_id+1

#finished CTs
n = 2
for i in range(10):
    radio_id = 1
    image = "%d.jpg"%(n)
    report = "something"
    status = "finished"
    cur.execute('insert into CT values(%d,%d,%d,"%s","%s","%s")'%(CT_id,n,radio_id,image,report,status))
    CT_id = CT_id+1
    string = f''' '''
    n = n+1


conn.commit()
cur.close()
conn.close()