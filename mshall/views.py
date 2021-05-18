from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallerypics, Champs2020to2021tech, Champs2011to2012sports, Champs2012to2013socult, Champs2016to2017sports, Champs2017to2018sports, Champs2018to2019sports, Champs2019to2020socult, Champs2019to2020tech

# Create your views here.

def home(request) :
    return render(request, 'msh/home/index.html')

def gallery(request) :
    pics = Gallerypics.objects.all()
    return render(request, 'msh/gallery/index1.html', {'pics': pics})

def hof(request) :
    champs20t = Champs2020to2021tech.objects.all()
    champs11s = Champs2011to2012sports.objects.all()
    champs12c = Champs2012to2013socult.objects.all()
    champs16s = Champs2016to2017sports.objects.all()
    champs17s = Champs2017to2018sports.objects.all()
    champs18s = Champs2018to2019sports.objects.all()
    champs19c = Champs2019to2020socult.objects.all()
    champs19t = Champs2019to2020tech.objects.all()
    return render(request, 'msh/hall of fame/index3.html', {'champs20t': champs20t, 'champs11s': champs11s, 'champs12c': champs12c, 'champs16s': champs16s, 'champs17s': champs17s, 'champs18s': champs18s, 'champs19c': champs19c, 'champs19t': champs19t})

def halln(request) :
    return render(request, 'msh/notice/index3.html')

def gcn(request) :
    return render(request, 'msh/notice/index4.html')

def messn(request) :
    return render(request, 'msh/notice/index5.html')

def genn(request) :
    return render(request, 'msh/notice/index6.html')