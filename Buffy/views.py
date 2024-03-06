from django.shortcuts import render
from .models import MyModel

# Create your views here.
def index(request):
    data =   ["item1", "item2", "item3"]               # MyModel.objects.all()
    return render(request, 'index.html', {'data': data})