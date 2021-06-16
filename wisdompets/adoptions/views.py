from django.shortcuts import render
from django.http import Http404
#from django.http import HttpResponse

from .models import Pet

def home(requests):
    #return HttpResponse('<p>Hello</p>')
    pets = Pet.objects.all()
    return render(requests, 'home.html', {
        'pets': pets,
    })

def pet_detail(requests, pet_id):
    #return HttpResponse('<p>pet_detail view with id {pet_id}</p>')   
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet Not Found')
    return render(requests, 'pet_detail.html', {
        'pet': pet,
    })