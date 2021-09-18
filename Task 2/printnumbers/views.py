from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'printnumbers/index.html')
def print(request):
    val=int(request.GET["num"])
    if(val>=0):
        check=False
        values=[i for i in range(1,val+1)]
    else:
        check=True
        values=[]
    return render(request,'printnumbers/print.html',{"values":values,"val":val,"check":check})