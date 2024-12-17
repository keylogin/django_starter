# import the standard Django Forms
# from built-in library
from django import forms 

# import LastModel from models.py
from .models import LastModel
  
# creating a form  
class LastForm(forms.ModelForm):
    
    class Meta:
        model = LastModel
        fields = "__all__"