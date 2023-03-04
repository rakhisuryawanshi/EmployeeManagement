from django.db import models 

class EmployeeManagement(models.Model):
    First_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    EmailId=models.CharField(max_length=40)
    Mobile=models.IntegerField()
    Address=models.CharField(max_length=30)
    Blood_Group=models.CharField(max_length=30)

    def __str__(self):
       return str(self.First_name) + " ["+str(self.Mobile)+']'