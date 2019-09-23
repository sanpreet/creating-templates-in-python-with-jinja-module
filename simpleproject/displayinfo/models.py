from django.db import models

# Create your models here.
# this is the class/table created which has the below attributes
# attribute 1: name
# attribute 2: occupation
# attribute 3: aim
class PersonInfo(models.Model):
    name = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)
    aim = models.TextField()
    
    def __str__(self):
        return self.name

        