from django.shortcuts import render,HttpResponse
from .models import *


def gallery(request):
    context = dict()
    context['imgs'] = Image.objects.all()
    return render(request, 'ture/gallery.html' , context=context )


def main_page(request):
    context = dict()
    context['tours'] = Tour.objects.all()
    context['attractions'] = Attraction.objects.all()
    return render(request, 'ture/index.html' , context=context)
    

def tour(request,id):
    context = dict()
    context['tour'] = Tour.objects.get(pk=id)
    context['tour_imgs'] = Image.objects.filter(tour_id_id = id)[:6]
    context['tour_attractions'] = Attraction.objects.filter(tour_id_id = id)
    
    return render(request , 'ture/ture.html' , context=context)

def about(request):
    return HttpResponse(f"<h1>About</h1>" )


