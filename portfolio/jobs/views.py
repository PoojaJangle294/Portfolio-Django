from django.shortcuts import render

from .models import jobs


# Create your views here.

def jhome(request):
    j=jobs.objects.all()
    return render(request,'jobs/jhome.html',{'j':j})

