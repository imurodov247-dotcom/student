from django.db import models


class Student(models.Model):
    name = models.CharField()
    yoshi = models.ImageField()
    kurs = models.CharField()
    guruhi = models.IntegerField()
    universitet = models.CharField()
    
    
    
    def __str__(self):
        return f"{self.name} (course {self.kurs})"
