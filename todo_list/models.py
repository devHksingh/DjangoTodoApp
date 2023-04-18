from django.db import models

# Create your models here.

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    # first_name =
    # Last_name = 
    # email = 
    def __str__(self):
        return self.item +' | ' +str(self.completed)