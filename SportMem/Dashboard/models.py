from django.db import models

class Dash(models.Model):
    SportName = models.CharField(max_length=100)
    NoOfMembers = models.IntegerField()
    def __str__(self):
        return self.SportName   
