from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
import random

def index(request):
#    all_cards = Card.objects.order_by('-id')
#    random_idx = random.randint(1, Card.objects.count())
#    random_obj = Card.objects.all()[random_idx]
#    random_card = Card.objects.get(pk=random_idx)
#    context = {'random_card': random_card}
#    return render(request, 'index.html', context)
	count = Card.objects.all().count()
        index = random.random() * (count - 1)
        int_index = int(round(index, 0))
        random_card = Card.objects.all()[int_index]
        context = {'random_card': random_card, 'int_index': (int_index + 1), 'count': count}
        return render(request, 'index.html', context)

def home(request):
	return render(request, 'home.html')
		
#	return render(request, 'index.html')


#	return HttpResponse("Hello world!  This is the flashcards index")

# Create your views here.
