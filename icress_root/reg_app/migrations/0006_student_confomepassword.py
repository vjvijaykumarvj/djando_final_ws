# Generated by Django 4.0 on 2022-02-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0005_remove_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='confomepassword',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
