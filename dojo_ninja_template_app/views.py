from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja
# Create your views here.
def index(request):
    context = {
        'all_dojos' : Dojo.objects.all(),
    }

    return render(request, "index.html", context)

def create_dojo(request):
    if request.method=="POST":
        Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
        return redirect('/')
    return redirect('/')

def create_ninja(request):
    if request.method=="POST":
        Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo_id=request.POST['dojo'])

    return redirect('/')

def delete_dojo(request):
    if request.method=="POST":
        this_dojo = Dojo.objects.get(id=request.POST['delete_id'])
        # Dojo.objects.delete(this_dojo)
        this_dojo.delete()

    return redirect('/')