from django.db import models

# def __init__(self, *args, **kwargs):
#         super(stud, self).__init__(*args, **kwargs)
# # Create your models here.
class stud(models.Model):
    roll = models.CharField(max_length =10)
    name = models.CharField(max_length =30)
    parentName = models.CharField(max_length =50)
    course = models.CharField(max_length =50)
    branch = models.CharField(max_length =50)
    def __str__(self):
        return self.roll
    class Meta:
        db_table='Stud_data'

class marks(models.Model):
    roll = models.CharField(max_length =10)
    subject1 = models.CharField(max_length =10)
    maxMarkSub1	= models.IntegerField()
    markObSub1 = models.IntegerField()
    subject2 = models.CharField(max_length =10)
    maxMarkSub2 = models.IntegerField()
    markObSub2 = models.IntegerField()
    subject3 = models.CharField(max_length =10)
    maxMarkSub3 = models.IntegerField()
    markObSub3 = models.IntegerField()
    subject4 = models.CharField(max_length =10)
    maxMarkSub4	= models.IntegerField()
    markObSub4	= models.IntegerField()
    subject5 = models.CharField(max_length =10)
    maxMarkSub5 = models.IntegerField()
    markObSub5 = models.IntegerField()
    subject6 = models.CharField(max_length =10)
    maxMarkSub6 = models.IntegerField()
    markObSub6 = models.IntegerField()
  
    def __str__(self):
        return self.roll
    class Meta:
        db_table='Stud_marks'

