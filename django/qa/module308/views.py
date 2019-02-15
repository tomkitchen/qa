from django.shortcuts import render
from django.http import HttpResponse
from .models import Module308Card
import random


# Create your views here.
def index(request):
#	random_idx = random.randint(1, Module308Card.objects.count())
    	count = Module308Card.objects.all().count()
	index = random.random() * (count - 1)
	int_index = int(round(index, 0))
	random_card = Module308Card.objects.all()[int_index]
    	context = {'random_card': random_card, 'int_index': (int_index + 1), 'count': count}
    	return render(request, 'index.html', context)
