from django.db import models

# Create your models here.


# class Person(models.Model):
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)


class UserData(models.Model):
    id=models.AutoField(primary_key=True)
    caller_id=models.IntegerField(default=0)
    first_name = models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    test = models.CharField(max_length=25)

    class Meta:
        db_table = 'UserData'
