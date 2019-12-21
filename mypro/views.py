
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return HttpResponse("hello,这是我的app!")


    
