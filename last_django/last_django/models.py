# import the standard Django Model
# from built-in library
from django.db import models

# declase a new model with a name "LastModel"
class LastModel(models.Model):
               # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to = 'images/')
    
    def __str__(self):
        return self.title