from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

def index(request):
    page = render(request, 'FirstPage.html')
    return page
