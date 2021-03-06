# Generated by Django 3.0.2 on 2020-02-03 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('account', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(default='123456', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('student_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('class_id', models.CharField(max_length=200)),
                ('password', models.CharField(default='123456', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('teacher_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(default='123456', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='common.Course')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='common.Student')),
            ],
            options={
                'unique_together': {('course', 'student')},
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('sign', models.CharField(default='否', max_length=8)),
                ('reason', models.CharField(max_length=200)),
                ('student_course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.StudentCourse')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='common.Course')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='common.Teacher')),
            ],
            options={
                'unique_together': {('course', 'teacher')},
            },
        ),
    ]
