from django.shortcuts import render

# Create your views here.
from  .models import Emp
def home(request):
    e=Emp.objects.all()
    return render(request,'emp/jhome.html',{'e':e})