from django.db import models

class UserModel(models.Model):
    User_ID=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.CharField(max_length=100)
    PhoneNumber=models.IntegerField()
    class Meta:
        db_table = 'dvgd_3_12\".\"user'


