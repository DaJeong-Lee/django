from django.shortcuts import render, HttpResponse
import json
import requests
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return HttpResponse('Hello world')

def profile(request):
    jsonLIst = []
    req = requests.get('https://api.github.com/users/dajeong-lee')
    jsonLIst.append(json.loads(req.content))
    parseData = []
    userData = {}
    for data in jsonLIst:
        userData['name'] = data['name']
        userData['email'] = data['email']
        parseData.append(userData)

    return HttpResponse(parseData)

def login(request):
    return render(request, 'app/base.html')

def facebook(request):
    return render(request, 'app/facebook.html')
