from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomePage(request):
    context = {}
    return render(request, 'page/home.html', context)