import json
import pprint

from django.contrib.sites import requests
from django.http import JsonResponse
from common.models import Manager, Student, Teacher


# CRUD（create, read, update, delete）


def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'manager_login':
        return manager_login(request)
    elif action == 'list_student':
        return list_student(request)
    elif action == 'list_teacher':
        return list_teacher(request)
    elif action == 'reset_password':
        return reset_password(request)
    elif action == 'manager_reset_password':
        return manager_reset_password(request)
    else:
        return JsonResponse({'ret': 1, 'msg': "error"}, json_dumps_params={'ensure_ascii': False})


def manager_login(request):
    manager_id = request.params['account']
    password = request.params['password']
    try:
        manager = Manager.objects.get(manager_id=manager_id)
    except Manager.DoesNotExist:
        return JsonResponse({'ret': 2}, json_dumps_params={'ensure_ascii': False})
    if password == manager.password:
        return JsonResponse({'ret': 0}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'ret': 1}, json_dumps_params={'ensure_ascii': False})


def list_student(request):
    try:
        students = Student.objects.filter().order_by("student_id")
        ret = []
        for student in students:
            ret.append(student.json())
        return JsonResponse({'ret': 0, 'data': ret}, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({'ret': 500, 'msg': '服务端发生异常！'}, json_dumps_params={'ensure_ascii': False})


def list_teacher(request):
    try:
        teachers = Teacher.objects.filter().order_by("teacher_id")
        ret = []
        for teacher in teachers:
            ret.append(teacher.json())
        return JsonResponse({'ret': 0, 'data': ret}, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({'ret': 500, 'msg': '服务端发生异常！'}, json_dumps_params={'ensure_ascii': False})


def reset_password(request):
    print(request.params)
    if request.params['user'] == 'student':
        try:
            student = Student.objects.get(student_id=request.params['student_id'])
            student.password = request.params['student_password']
            student.class_id = request.params['student_class_id']
            student.name = request.params['student_name']
            student.save()
            return JsonResponse({'ret': 0, 'data': "修改成功"}, json_dumps_params={'ensure_ascii': False})
        except Student.DoesNotExist:
            return JsonResponse({'ret': 1, 'data': "学号为" + request.params['student_id'] + "该学生信息不存在"}, json_dumps_params={'ensure_ascii': False})
    else:
        try:
            teacher = Teacher.objects.get(teacher_id=request.params['teacher_id'])
            teacher.name = request.params['teacher_name']
            teacher.password = request.params['teacher_password']
            teacher.email = request.params['teacher_email']
            teacher.save()
            return JsonResponse({'ret': 0, 'data': "修改成功"}, json_dumps_params={'ensure_ascii': False})
        except Teacher.DoesNotExist:
            return JsonResponse({'ret': 1, 'data': "学号为" + request.params['teacher_id'] + "该学生信息不存在"},
                                json_dumps_params={'ensure_ascii': False})


def manager_reset_password(request):
    manager_id = request.params['manager_id']
    password = request.params['password']
    try:
        manager = Manager.objects.get(manager_id=manager_id)
        manager.password = password
        manager.save()
    except Manager.DoesNotExist:
        return JsonResponse({'ret': -1, "msg": "该学生不存在"}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'ret': 0}, json_dumps_params={'ensure_ascii': False})
