# Hospital Management System with AI-based Radiology Diagnosis

## Introduction
- This is the team project for CUHKSZ's CSC4001 course.
- It is developed by CUHKSZ students: Yaling Shen, Yuzhe Jin, Yuan Gao, Zeyu Zhou.
- The project aims to use the latest scientific research achievements, CT image report generation algorithm, and integrate it into the hospital management system, to explore the possible development path of the hospital in the future.

## Technology Stack
- Frontend
   - Vue.js
   - Element UI
   - Echarts
- Backend
   - Flask
   - Pytorch
- DB
   - MySQL
- Server
   - Baidu Cloud Server

## How to install
```
cd back
pip install

cd front
npm install
```

## How to run
```
cd back
python app.py

cd front
npm run dev
```
## Role Management
- Super Admin
- Patient
- Outpatient Doctor
- Radiologist

# User Manual
## Super Admin
- Workbench
   - View User Infomation
   - Change Account Role

## Patient
- Dashboard
   - Check how many people's orders are ahead of him/her.
   - Check how much time he/she should wait for the CT image report.
- Appointment
   - Check all the doctors working today and their basic information.
   - Make appointment with any available doctor.

## Outpatient Doctor
- Dashboard
   - Show the real time.
   - Check how many patients are there visiting for the specific day.
   - Check how many patients are waiting for CT image report.
   - Check how many patients have finished their appointments.
- Patient List
   - Show all patients' information.
   - Input Diagnosis for a specific patient.
   - Arrange CT image service for a patient.
   - Check CT image report.
   - Terminate the appointment.
- Profile
   - Check his/her own basic information

## Radiologist
- Dashboard
   - Show the real time.
   - Check how many patients are there visiting for the specific day.
   - Check how many patients are waiting for CT image report.
   - Check how many patients have finished their appointments.
- Patient List
   - Show all patients' information.
   - Check Diagnosis.
   - Turn to the workbench page.
- Workbench
   - Upload CT image report.
   - Generate report automatically by algorithm.
   - Upload the report.

