# Generated by Django 4.0.3 on 2022-09-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_address_engineering_colleges_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design_colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_Name', models.CharField(max_length=150)),
                ('Fee', models.CharField(max_length=100)),
                ('Exam', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Img', models.CharField(max_length=500)),
                ('Rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Law_colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_Name', models.CharField(max_length=150)),
                ('Fee', models.CharField(max_length=100)),
                ('Exam', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Img', models.CharField(max_length=500)),
                ('Rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Management_colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_Name', models.CharField(max_length=150)),
                ('Fee', models.CharField(max_length=100)),
                ('Exam', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Img', models.CharField(max_length=500)),
                ('Rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medical_colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_Name', models.CharField(max_length=150)),
                ('Fee', models.CharField(max_length=100)),
                ('Exam', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Img', models.CharField(max_length=500)),
                ('Rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Science_colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_Name', models.CharField(max_length=150)),
                ('Fee', models.CharField(max_length=100)),
                ('Exam', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Img', models.CharField(max_length=500)),
                ('Rating', models.CharField(max_length=50)),
            ],
        ),
    ]