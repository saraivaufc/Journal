from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	
