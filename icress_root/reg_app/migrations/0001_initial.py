# Generated by Django 4.0 on 2022-02-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Contact_Number', models.IntegerField()),
                ('Email_id', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Courseintrested', models.CharField(max_length=100)),
                ('python', models.CharField(max_length=100)),
                ('Django', models.CharField(max_length=100)),
                ('Java', models.CharField(max_length=100)),
                ('Bigdata', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]