from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs!")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, my_val):
    return HttpResponse(f"placeholder to display blog number: { my_val }")

def edit(request, my_val):
    return HttpResponse(f"placeholder to edit blog {my_val}")

def destroy(request, my_val):
    return redirect('/')