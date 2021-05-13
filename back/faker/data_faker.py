#!/usr/bin/python
# -*- coding: UTF-8 -*-
from faker import Faker
import pymysql
import random
import pandas

conn = pymysql.connect(host = '182.61.17.45', 
                       user = "csc4001",
                       passwd = "123456", 
                       database = "Hospital")
cur = conn.cursor()

fake = Faker(locale = "en_US")
genders = ['M','F']
allergies = ['penicillin','aspirin','penicillin, aspirin','none','none','none','none','none','none','none','none','none']
departments = ['Department of internal medicine','Department of surgery','Department of pediatrics','Department of obstetrics and gynecology',
            'Department of neurology', 'Department of ophtalmology' , 'E.N.T.department', 'Department of stomatology', 'Department of urology',
            'Department of orthopedic', 'Department of traumatology','Department of endocrinology','Department of anesthesiology',
            'Department of dermatology' ,'Department of infectious diseases','Department of pathology', 'Department of psychiatry', 
            'Department of orthopacdic surgery','Department of cardiac surgery','Department of cerebral surgery','Department of thoracic surgery']
buildings = ['A','B','C','D']
titles = ['Chief physician', 'Vice chief physician', 'Vice chief physician', 'Attending physician', 'Attending physician', 
        'Attending physician', 'Attending physician', 'Attending physician', 'Attending physician', 'Attending physician']

for i in range(100):
    id_ = int(fake.ssn().replace('-',''))
    name = fake.name()
    birth = fake.date(pattern="%Y-%m-%d", end_datetime=None) 
    gender = random.choice(genders)
    home_add = fake.address()
    phone = fake.phone_number()
    allergies = random.choice(allergies)

    account = fake.user_name()[:16]
    password = fake.password(length=random.randint(8,16), special_chars=True, digits=True, upper_case=True, lower_case=True)

    cur.execute('insert into Patient values (%d, "%s", "%s", "%s", "%s", "%s", "%s")'%(id_,name,birth,gender,home_add,phone,allergies))
    cur.execute('insert into Account values ("%s","%s", %d,"patient")'%(account,password,id_))

for i in range(100):
    id_ = int(fake.ssn().replace('-',''))
    name = fake.name()
    gender = random.choice(genders)
    phone = fake.phone_number()
    department = random.choice(departments)
    office = "Building %s Room %d"%(random.choice(buildings), random.randint(101,599))
    title = random.choice(titles)
    specialty = 'None'

    account = fake.user_name()[:16]
    password = fake.password(length=random.randint(8,16), special_chars=True, digits=True, upper_case=True, lower_case=True)

    cur.execute('insert into Out_doctor values (%d, "%s", "%s", "%s", "%s", "%s", "%s", "%s")'%(id_,name,gender,phone,department,office,title,specialty))
    cur.execute('insert into Account values ("%s","%s", %d,"outpatient doctor")'%(account,password,id_))

for i in range(50):
    id_ = int(fake.ssn().replace('-',''))
    name = fake.name()
    gender = random.choice(genders)
    phone = fake.phone_number()
    office = "Building %s Room %d"%(random.choice(buildings), random.randint(101,599))

    account = fake.user_name()[:16]
    password = fake.password(length=random.randint(8,16), special_chars=True, digits=True, upper_case=True, lower_case=True)

    cur.execute('insert into Radiologist values (%d, "%s", "%s", "%s", "%s")'%(id_,name,gender,phone,office))
    cur.execute('insert into Account values ("%s","%s", %d,"radiologist")'%(account,password,id_))

conn.commit()
cur.close()
conn.close()