import json
import os
import time
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import transaction
import pprint
# from flask import Flask
# from flask import request

from django.contrib.sites import requests
from django.http import JsonResponse, FileResponse, HttpResponse
from werkzeug.utils import secure_filename

from common.models import Student, Course, StudentCourse, Attendance
from mgr import MyEncoder
# CRUD（create, read, update, delete）
from myMethod import face_recognize, subtract_time


def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method == 'POST':
        request.params = request.POST
    action = request.params['action']
    # elif request.method in ['POST', 'PUT', 'DELETE']:
    # # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
    # request.params = json.loads(request.body)

    # Better do not use this code "print(request.body)",
    # Otherwise, you will get a error: You cannot access body after reading from request's data stream

    if action == 'list_course':
        return list_course(request)
    elif action == 'student_login':
        return student_login(request)
    elif action == 'course_attendance':
        return course_attendance(request)
    elif action == 'list_not_modify':
        return list_not_modify(request)
    elif action == 'student_sign_in':
        return student_sign_in(request)
    elif action == 'student_get_portrait':
        return student_get_portrait(request)
    elif action == 'student_get_self_info':
        return student_get_self_info(request)
    elif action == 'request_for_leave':
        return request_for_leave(request)
    elif action == 'student_reset_password':
        return student_reset_password(request)
    else:
        return JsonResponse({'ret': 400, 'msg': '不支持该类型http请求'},json_dumps_params={'ensure_ascii':False})


@transaction.atomic
def student_login(request):
    student_id = request.params['account']
    password = request.params['password']
    try:
        student = Student.objects.get(student_id=student_id)
    except Student.DoesNotExist:
        return JsonResponse({'ret': 2}, json_dumps_params={'ensure_ascii': False})
    if password == student.password:
        return JsonResponse({'ret': 0}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'ret': 1}, json_dumps_params={'ensure_ascii': False})


@transaction.atomic
def list_course(request):
    try:
        student_id = request.params['account']
        student_courses = StudentCourse.objects.filter(student_id=student_id).values()
        ret = []
        for student_course in student_courses:
            for key, value in student_course.items():
                if "course_id" == key:
                    courses = Course.objects.filter(course_id=value)
                    for course in courses:
                        ret.append(course.json())
        return JsonResponse({'ret': 0, 'data': ret}, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({'ret': 500, 'msg': '服务端发生异常！'}, json_dumps_params={'ensure_ascii': False})


@transaction.atomic
def course_attendance(request):
    try:
        student_id = request.params['student_id']
        course_id = request.params['course_id']
        attendances = Attendance.objects.filter(student_id=student_id, course_id=course_id)
        ret = []
        for attendance in attendances:
            ret.append(attendance.json())
        return JsonResponse({'ret': 0, 'data': ret}, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({'ret': 500, 'msg': '服务端发生异常！'}, json_dumps_params={'ensure_ascii': False})


@transaction.atomic
def list_not_modify(request):
    try:
        student_id = request.params['student_id']
        attendances = Attendance.objects.filter(student_id=student_id, modify=0)
        ret = []
        for attendance in attendances:
            sign_time = attendance.time
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if subtract_time(sign_time, current_time) < 5:
                ret.append(attendance.json())
            else:
                attendance.modify = 1
                attendance.type = 3
                attendance.save()
        return JsonResponse({'ret': 0, 'data': ret}, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({'ret': 500, 'msg': '服务端发生异常！'}, json_dumps_params={'ensure_ascii': False})


@transaction.atomic
def student_sign_in(request):
    try:
        student_id = request.params['student_id']
        course_id = request.params['course_id']
        teacher_id = request.params['teacher_id']
        serial_number = request.params['serial_number']
        sign_type = request.params['type']
        try:
            attendance = Attendance.objects.get(student_id=student_id, course_id=course_id, teacher_id=teacher_id,
                                                serial_number=serial_number)
        except Attendance.DoesNotExist:
            return JsonResponse({'ret': 1, 'data': '该记录不存在!'}, json_dumps_params={'ensure_ascii': False})
        if sign_type == "0":
            # todo 超过事件范围就不能签到，只能请假
            sign_time = attendance.time
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # if subtract_time(sign_time, current_time) > 5:
            #     return JsonResponse({'ret': 2, 'data': '超过点名时间了! '}, json_dumps_params={'ensure_ascii': False})

            with request.FILES.get('image') as f:
                student_picture = "resources/picture/received/" + f.name + ".png"
                if os.path.exists(student_picture):
                    print(student_picture)
                    os.remove(student_picture)
                default_storage.save(student_picture, ContentFile(f.read()))
            path1 = 'D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\received\\'
            path2 = 'D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\native\\'
            path1 = path1 + f.name + ".png"
            path2 = path2 + f.name + ".png"
            coincidence = face_recognize(path1,path2)
            if coincidence < 50:
                # modify == 1 表示此次点名所有操作均已完成，无需改变
                attendance.modify = 1
                attendance.type = sign_type
                attendance.save()
                return JsonResponse({'ret': 0, 'data': '修改成功! '}, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse({'ret': 1, 'data': '识别失败! '}, json_dumps_params={'ensure_ascii': False})
        else:
            # modify == 2 表示处于请假状态，老师还未批准
            attendance.modify = 2
            attendance.type = sign_type
            attendance.save()
            return JsonResponse({'ret': 0, 'data': '修改成功! '}, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({'ret': 500, 'msg': '服务端发生异常！'}, json_dumps_params={'ensure_ascii': False})


def student_get_portrait(request):
    path = 'D:\\zuoye\\python\\attendanceSystem\\resources\\picture\\received\\'
    path = path + request.params["student_id"] + ".png"
    f = open(path, 'rb')
    return HttpResponse(f.read(), content_type='image/jpeg')


def student_get_self_info(request):
    student_id = request.params['student_id']
    print(student_id)
    try:
        student = Student.objects.get(student_id=student_id)
    except Student.DoesNotExist:
        return JsonResponse({'ret': -1, "msg": "该学生不存在"}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'ret': 0, 'student_name': student.name, 'student_class_id': student.class_id}, json_dumps_params={'ensure_ascii': False})


def request_for_leave(request):
    try:
        attendance = Attendance.objects.get(serial_number=request.params["serial_number"],student_id=request.params["student_id"], teacher_id=request.params["teacher_id"], course_id=request.params["course_id"])
        attendance.type = request.params["type"]
        attendance.modify = request.params["modify"]
        attendance.save()
        name = request.params["serial_number"] + request.params["student_id"] + request.params["teacher_id"] + request.params["course_id"]
        with request.FILES.get('image') as f:
            student_picture = "resources/picture/attendance/" + name + ".png"
            if os.path.exists(student_picture):
                print(student_picture)
                os.remove(student_picture)
            default_storage.save(student_picture, ContentFile(f.read()))
    except Attendance.DoesNotExist:
        return JsonResponse({'ret': -1, "msg": "该学生不存在"}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'ret': 0, "msg": "修改成功！"}, json_dumps_params={'ensure_ascii': False})


def student_reset_password(request):
    student_id = request.params['student_id']
    password = request.params['password']
    try:
        student = Student.objects.get(student_id=student_id)
        student.password = password
        student.save()
    except Student.DoesNotExist:
        return JsonResponse({'ret': -1, "msg": "该学生不存在"}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'ret': 0}, json_dumps_params={'ensure_ascii': False})
