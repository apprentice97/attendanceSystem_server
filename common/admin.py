from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Student, Teacher, Course, TeacherCourse, Attendance, Manager, StudentCourse


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'class_id', 'password')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name', 'password')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'name')


class TeacherCourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'teacher_name')


class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'course_name')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'student_name', 'course_name', 'teacher_name', 'modify', 'type', 'time')


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_id', 'password')


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(TeacherCourse, TeacherCourseAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)
