from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

from .models import Profile
from django.http import HttpResponse
def create(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        bio=request.POST['bio']
        new_profile=Profile(name=name,email=email,bio=bio)
        new_profile.save()

        return HttpResponse("User "+name+" created successfully")
    return HttpResponse("else")

from django.http import JsonResponse
import json
def jsondata(request):
    data=list(Profile.objects.values())
    return JsonResponse(data,safe=False)