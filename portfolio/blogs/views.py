from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Blogs
def bhome(request):
    b=Blogs.objects.all()
    return render (request,'blogs/bhome.html',{'b':b})

def detail(request,blog_id):
    blogdetail=get_object_or_404(Blogs,pk=blog_id)
    return render (request,'blogs/detail.html',{'blog':blogdetail})
