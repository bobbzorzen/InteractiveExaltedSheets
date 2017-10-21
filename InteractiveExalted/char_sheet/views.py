from django.shortcuts import render

def index(request):
    return render(request, 'char_sheet/home.html')

def cards(request):
    return render(request, 'char_sheet/cards.html')
