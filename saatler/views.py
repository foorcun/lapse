from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'saatler/home.html')





'''def index(request):
    return HttpResponse("<h2>HEYY!!111!!</h2>")
'''