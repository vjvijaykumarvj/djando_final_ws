# Generated by Django 4.0 on 2022-07-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('room_name', models.CharField(choices=[('superior king room', 'superior king room'), ('primior king room', 'primior king room'), ('double room with double beds', 'double room with double beds'), ('primior single room', 'primior single room')], default='superior king room', max_length=30)),
                ('room_image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('start_date', models.DateField()),
                ('is_available', models.BooleanField(default=True)),
                ('no_of_dats', models.IntegerField()),
            ],
        ),
    ]