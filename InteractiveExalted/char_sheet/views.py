from django.shortcuts import render

def index(request):
    return render(request, 'char_sheet/home.html')
