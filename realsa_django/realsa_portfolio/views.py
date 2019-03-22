from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'realsa_portfolio/index.html')

def realsa_blog(request):
    return render(request, 'realsa_blog/layout.html')

def contact(request):
    return render(request, 'realsa_portfolio/basic.html', {'basic_content':['If you want to contact me, email to','hendrik@hexagenic.com']})

def landing(request):
    return render(request, 'realsa_portfolio/landing.html')