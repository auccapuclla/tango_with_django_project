from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#client request this view and we send back this string 
#now we need to map this view to an URL, in the url.py file in the main project
def index(request):
    return HttpResponse("first view, handle url i think! Yep it is ! ")