from django.shortcuts import render
from .forms import LastForm

# Create your views here.
def home_view(request):
    context ={}
    context['form']= LastForm()
    return render(request, "home.html", context)