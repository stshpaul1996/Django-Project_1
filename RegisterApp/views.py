from django.shortcuts import render
from django.http import HttpResponse
from .models import RegisterDB
# Create your views here.

def register(request):
    if request.method == 'GET':
        fetchedData = RegisterDB.objects.all()
        
        return render(request, 'index.html', {'data': fetchedData})
    else:
        RegisterDB(fullname = request.POST.get('name'),
        email = request.POST.get('email'),
        mobile = request.POST.get('mobile'),
        address = request.POST.get('address')).save()
        fetchedData = RegisterDB.objects.all()
        return render(request, 'index.html', {'data': fetchedData})  

