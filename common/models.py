from django.db import models

# Create your models here.

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=200, primary_key=True)
    class_id = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default="123456")

    def __str__(self):
        return self.student_id + self.name

    def json(self):
        return {"student_id": str(self.student_id),
                "student_name": self.name, "class_id": self.class_id, "password": self.password}


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    teacher_id = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200, default="123456")
    email = models.CharField(max_length=200, default=" ")

    def __str__(self):
        return self.teacher_id + self.name

    def json(self):
        return {"teacher_id": str(self.teacher_id),
                "teacher_name": self.name, "password": self.password,
                "email": self.email}


class Course(models.Model):
    course_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.course_id) + self.name

    def json(self):
        return {"course_id": self.course_id, "name": self.name}


class TeacherCourse(models.Model):
    course = models.ForeignKey(Course,on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)

    class Meta:
        unique_together = ("course", "teacher")

    def __str__(self):
        return str(self.teacher) + "_" + str(self.course)

    def course_name(self):
        return self.course.name

    def teacher_name(self):
        return self.teacher.name


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    class Meta:
        unique_together = ("course", "student")

    def __str__(self):
        return str(self.student) + "_" + str(self.course)

    def student_id(self):
        return self.student_id() + ""

    def student_name(self):
        return self.student.name

    def course_name(self):
        return self.course.name


class Attendance(models.Model):
    serial_number = models.IntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, default='')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, default='')
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, default='')
    modify = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    time = models.CharField(max_length=200, default="2020.01.01")

    def __str__(self):
        return str(self.serial_number) + "_" + str(self.type) + "_" + str(self.time) + "_" + str(self.student) + "_" + str(self.course) + "_" + str(self.teacher)

    def json(self):
        return {"serial_number": str(self.serial_number),
                "student_id": self.student_id, "course_id": self.course_id, "teacher_id": self.teacher_id,
                "modify": str(self.modify), "type": str(self.type), "time": self.time,
                "student_name": self.student.name, "course_name": self.course.name, "teacher_name": self.teacher.name}

    def json_student_self(self):
        return {"serial_number": self.serial_number, "modify": self.modify, "type": str(self.type), 'time': self.time}

    def json_student_name(self):
        return {"serial_number": self.serial_number, "modify": self.modify, "type": str(self.type), 'time': self.time,
                'studentName': self.student.name}

    def student_name(self):
        return self.student.name

    def course_name(self):
        return self.course.name

    def teacher_name(self):
        return self.teacher.name

    def student_id(self):
        return self.student.id

    def course_id(self):
        return self.course.id

    def teacher_id(self):
        return self.course.id


class Manager(models.Model):
    manager_id = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200, default="123456")
