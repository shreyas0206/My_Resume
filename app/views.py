from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    return render(request,'home.html')
# def c_one(request):
#     return render(request,'certificate_1.html')
def project(request,pk):
    data=Project.objects.get(pk=pk)
    return render(request,'project1.html',{"pk":pk,'data':data})
def project2(request,pk):
    data=Project.objects.get(pk=pk)
    return render(request,'project2.html',{"pk":pk,'data':data})
def project3(request,pk):
    data=Project.objects.get(pk=pk)
    return render(request,'project3.html',{"pk":pk,'data':data})
