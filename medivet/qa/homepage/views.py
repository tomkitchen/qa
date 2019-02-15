from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')
		
#	return render(request, 'index.html')


#	return HttpResponse("Hello world!  This is the flashcards index")

# Create your views here.
