from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
import datetime


def home(request):
    data = {}
    data['transactions'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'account/home.html', data)

def listagem(request):
    data = {}
    data['transactions'] = Transactions.objects.all()
    # data['transactions'] = Transactions.objects.filter()
    # data['transactions'] = Transactions.objects.last()
    return render(request, 'account/listagem.html', data)