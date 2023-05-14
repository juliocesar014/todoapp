from .models import Task
from .serializer import TaskSerializer
from rest_framework import viewsets
class ListTaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
