from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
import random


# Create your views here.
def ccnp(request, chpt):
	chapter_objs = Card.objects.all().filter(chapter = chpt)
	chapters = Card._meta.get_field('chapter').choices
#	random_idx = random.randint(1, chapter_objs.objects.count())
    	count = chapter_objs.count()
	index = random.random() * (count - 1)
	int_index = int(round(index, 0))
#	random_card = Card.objects.all()[int_index]
	random_card = chapter_objs[int_index]
    	context = {'random_card': random_card, 'chapters': chapters, 'count': count, 'int_index': int_index + 1}
    	return render(request, 'ccnp.html', context)

def check_card(request, chpt, qnum):
	chapter_objs = Card.objects.all().filter(chapter = chpt)
        chapters = Card._meta.get_field('chapter').choices
        count = chapter_objs.count()
        index = (int(qnum) - 1)
        int_index = int(round(index, 0))
	random_card = chapter_objs[int_index]
        context = {'random_card': random_card, 'chapters': chapters, 'count': count, 'int_index': int_index + 1}
        return render(request, 'ccnp.html', context)

def check_card_text(request, chpt, qtext):
        chapter_objs = Card.objects.all().filter(chapter = chpt, question__contains = qtext)
        chapters = Card._meta.get_field('chapter').choices
        count = chapter_objs.count()
	index = random.random() * (count - 1)
        int_index = int(round(index, 0))
#        int_index = int(round(index, 0))
        random_card = chapter_objs[int_index]
        context = {'random_card': random_card, 'chapters': chapters, 'count': count, 'int_index': int_index + 1}
        return render(request, 'ccnp.html', context)

