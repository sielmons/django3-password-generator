from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'moncef_generator/home.html')
def password(request):
    
    characters = list("abcdefghijklmnopqrstuvwxyz")
    
    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIKLM?OPQRSTUVWXYZ"))

    if request.GET.get('specials'):
        characters.extend(list("@ùµ"))

    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))

    length = int(request.GET.get('length', 10 ))

    thepassword= ''
    for i in range(length):
        thepassword+=random.choice(characters)

    return render(request, 'moncef_generator/password.html', {'password':thepassword})


def about(request):
    return render(request, 'moncef_generator/about.html')
