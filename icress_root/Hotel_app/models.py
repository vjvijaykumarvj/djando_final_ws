from django.db import models

# Create your models here.

rooms_list = [('superior king room','superior king room'),
              ('primior king room','primior king room'),
              ('double room with double beds','double room with double beds'),
              ('primior single room','primior single room')]
class Rooms(models.Model):
    username = models.CharField(max_length=20)
    room_no = models.IntegerField()
    room_name = models.CharField(max_length=30,choices=rooms_list,default='superior king room')
    room_image = models.ImageField(upload_to='media',null=True,blank=True)
    start_date = models.DateField(auto_now=False,auto_now_add=False)
    is_available = models.BooleanField(default=True)
    no_of_dats = models.IntegerField()

    def __str__(self):
        return 'Room Number :' + str(self.room_no)

