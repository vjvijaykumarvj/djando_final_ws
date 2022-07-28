from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_CATAGERIES=(
        ('YAC' , 'AC'),
        ('NAC' , 'NON-AC'),
        ('DEL' , 'DELUXE'),
        ('KIN' , 'KING'),
        ('QUE' , 'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3,choices=ROOM_CATAGERIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}.{self.category} with{self.beds} for {self.capacity} people'
