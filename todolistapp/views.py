from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
class TaskList(ListView):
    model = Task
    template_name = 'todolistapp/task_list.html'
     