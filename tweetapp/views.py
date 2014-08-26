from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django import forms
from tweetapp.models import NewUser, NewUserForm

# Create your views here.

# def home(request):
#     return HttpResponse("Hello, world")


def index(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        form.save()
    else:
        form = NewUserForm()
    
    return render(request, 'index.html', {'form': form})