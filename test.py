import datetime
import json
import time

import requests
import pprint

from common.models import Attendance
from myMethod import face_recognize, face_recognizes, subtract_time

# urlStudent = 'http://192.168.137.1/mgr/student/'
# urlTeacher = 'http://192.168.137.1/mgr/teacher/'




#测试学生的查询
# response = requests.get('http://localhost/mgr/student/?action=list_students')
# print(response.text)
# http://192.168.137.1/mgr/student/?action=list_students
# http://192.168.137.1/mgr/student/?action=student_login&account=B16041735&password=123456

# http://192.168.137.1/mgr/student/?password=123456&action=student_login&account=B16041735
# response = requests.get('http://192.168.137.1/mgr/student/?password=123456&action=student_login&account=B16041735')
# print(response.text)


# payload = {
#     'action': 'student_login',
#     'account': 'B16041735',
#     'password': '123456'
# }
# response = requests.post('http://192.168.137.1/mgr/student/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'teacher_login',
#     'account': 'T040001',
#     'password': '123456'
# }
# response = requests.get('http://192.168.137.1/mgr/teacher/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'manager_login',
#     'account': 'M2',
#     'password': '123455'
# }
# response = requests.post('http://192.168.137.1/mgr/manager/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'list_course',
#     'account': 'B16041735',
#     'password': '123456'
# }
# response = requests.post('http://192.168.137.1/mgr/student/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'course_attendance',
#     'student_id': 'B16041735',
#     'course_id': 'C040001'
# }
# response = requests.post('http://192.168.137.1/mgr/student/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'list_not_modify',
#     'student_id': 'B16041735',
# }
# response = requests.post('http://192.168.137.1/mgr/student/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'student_sign_in',
#     'student_id': 'B16041732',
#     'course_id': 'C040004',
#     'teacher_id': 'T040003',
#     'serial_number': '1',
#     'type': '3'
# }
# response = requests.post('http://192.168.137.1/mgr/student/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'list_course',
#     'account': 'T040004',
#     'password': '123456'
# }
# response = requests.post('http://192.168.137.1/mgr/teacher/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'course_information',
#     'teacher_id': 'T040004',
#     'course_id': 'C040003'
# }
# response = requests.post('http://192.168.137.1/mgr/teacher/', data=json.dumps(payload))
# pprint.pprint(response.text)

# payload = {
#     'action': 'course_attendance',
#     'teacher_id': 'T040004',
#     'course_id': 'C040003'
# }
# response = requests.post('http://192.168.137.1/mgr/teacher/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'course_attendance_information',
#     'teacher_id': 'T040004',
#     'course_id': 'C040003',
#     'serial_number': '1'
# }
# response = requests.post('http://192.168.137.1/mgr/teacher/', data=json.dumps(payload))
# pprint.pprint(response.text)

# payload = {
#     'action': 'call_name',
#     'teacher_id': 'T040004',
#     'course_id': 'C040004'
# }
# response = requests.post('http://192.168.137.1/mgr/teacher/', data=json.dumps(payload))
# print(response.text)

# payload = {
#     'action': 'student_get_self_info',
#     'teacher_id': 'B1604735'
# }
# response = requests.post('http://192.168.137.1/mgr/student/', data=json.dumps(payload))
# print(response.text)

# params = {
#     'action': 'student_get_self_info',
#     'student_id': 'B16041735'
# }
# response = requests.get(url=urlStudent, params=params)
# print(response.text)

# path1 = 'D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\received\\B16041734.png'
# path2 = 'D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\native\\B16041733.png'
# face_recognize(path1, path2)


