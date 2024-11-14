from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    email = models.EmailField()
    college_code = models.IntegerField()

    def __str__(self):
        return self.first_name+ " "+self.last_name