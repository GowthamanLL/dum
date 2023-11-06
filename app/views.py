from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import new
from django.urls import reverse
# Create your views here.
def index(request):
    return HttpResponse("hello world")
def index2(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())
def index3(request):
    n=new.objects.all().values()
    out=""
    for i in n:
        out+=i['name']+str(i['age'])
    return HttpResponse(out)

def index4(request):
    n=new.objects.all().values()
    templates=loader.get_template("index2.html")
    context={
        "members":n
    }
    return HttpResponse(templates.render(context,request))

def add(request):
    template=loader.get_template("add.html")
    return HttpResponse(template.render({},request))

def addrecord(request):
    x=request.POST['name']
    y=request.POST['age']
    m=new(name=x,age=y)
    m.save()
    return HttpResponseRedirect(reverse('index4'))
def delete(request,id):
    n=new.objects.get(id=id)
    n.delete()
    return HttpResponseRedirect(reverse('index4'))
def update(request,id):
    n=new.objects.get(id=id)
    template=loader.get_template('update.html')
    return HttpResponse(template.render({"member":n},request))
def updaterecord(request,id):
    n=new.objects.get(id=id)
    x=request.POST['name']
    y=request.POST['age']
    n.name=x
    n.age=y
    n.save()
    return HttpResponseRedirect(reverse('index4'))