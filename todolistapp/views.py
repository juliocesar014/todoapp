from django.shortcuts import render
from django.http import HttpResponse

def taskList(request):
    return HttpResponse("Hello, world. You're at the task list!")