from django.db import models
# Create your models here.

class Developer(models.Model):
    name=models.CharField(max_length=100)
       
       def __Str__( request):
        return self.name



class Game(models.Model):
    title=models.CharField(max_length=100)
    developer=models.Foreignkey(Developer,on_delete=models.CASCEDE)
       def __Str__(request):
        return self.title
