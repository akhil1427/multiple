from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def akhil(request):
    return HttpResponse('<center><h1> This is created by HttpResponse </h1></center>')

def page(request):
    return render(request,'page.html')
    
