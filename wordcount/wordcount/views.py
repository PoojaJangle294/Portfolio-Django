from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return  render(request,'jhome.html',{'name':'Spark'})
    # return  HttpResponse("<h2 style='color:red'>Welcome to Django Page!!</h2>")
    if request.method=="POST":
        n1=int(request.POST.get('t1'))
        n2=int(request.POST.get('t2'))
        btn=request.POST.get("btn")
        if btn=="add":
            return  render(request,'jhome.html',{'result':n1+n2,'n1':n1,'n2':n2})
        elif btn=="sub":
            return  render(request,'jhome.html',{'result':n1-n2,'n1':n1,'n2':n2})
        elif btn=="mul":
            return  render(request,'jhome.html',{'result':n1*n2,'n1':n1,'n2':n2})
        elif btn=="div":
            return  render(request,'jhome.html',{'result':n1/n2,'n1':n1,'n2':n2})
    else:
        return render(request,'jhome.html',{"name":"spark"})

def about(request):
    return render(request, 'about.html')
    # return  HttpResponse("<h2 style='color:blue'>This is about  Page!!</h2>")

def contact(request):
    return render(request, 'contact.html')
    # return  HttpResponse("<h2 style='color:orange'>This contact  Page!!</h2>")

def cal(request):
    print()
    # if request.method=="POST":
    #     n1=int(request.POST.get('t1'))
    #     n2=int(request.POST.get('t2'))
    #     btn=request.POST.get("btn")
    #     if btn=="add":
    #         return  render(request,'jhome.html',{'result':n1+n2})
    #     elif btn=="sub":
    #         return  render(request,'jhome.html',{'result':n1-n2})
    #     elif btn=="mul":
    #         return  render(request,'jhome.html',{'result':n1*n2})
    #     elif btn=="div":
    #         return  render(request,'jhome.html',{'result':n1//n2})
    # else:
    #     return render(request,'jhome.html',{"name":"spark"})



    # n1=int(request.POST.get('t1'))
    # n2=int(request.POST.get('t2'))
    # btn=request.POST.get("btn")
    #
    # if btn=="add":
    #     return  render(request,'cal.html',{'result':n1+n2})
    # elif btn=="sub":
    #     return  render(request,'cal.html',{'result':n1-n2})
    # elif btn=="mul":
    #     return  render(request,'cal.html',{'result':n1*n2})
    # elif btn=="div":
    #     return  render(request,'cal.html',{'result':n1//n2})

def word(request):
    return render(request, 'word.html')

def count(request):
    val1 = request.GET.get('chk1','off')
    val2 = request.GET.get('chk2', 'off')
    val3 = request.GET.get('chk3', 'off')
    val4 = request.GET.get('chk4', 'off')
    val5 = request.GET.get('chk5', 'off')
    data=request.GET.get('txt')
    # return render(request, 'count.html',{'info':data})
    if val1=='on':
        params={'purpose':"Information","result":data}
        return render (request,'count.html',params)
    elif val2=='on':
        word_list=data.split()
        word_len=len(word_list)
        params={"purpose":"Word Counnt","result":word_len}
        return render(request, 'count.html', params)
    elif val3=='on':
        word_list=data.split()
        word_len=len(word_list)
        params={"purpose":"Word Counnt","result":word_len}
        return render(request, 'count.html', params)
    elif val4=='on':
        up=data.uppercase()
        params={"purpose":"Word Uppercase","result":up}
        return render(request, 'count.html', params)
    elif val5=='on':
        word_list=data.split()
        word_len=len(word_list)
        params={"purpose":"Word Counnt","result":word_len}
        return render(request, 'count.html', params)
