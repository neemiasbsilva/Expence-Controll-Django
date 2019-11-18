from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
import datetime
from .form import TransactionsForm


def home(request):
    data = {}
    data['transactions'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'account/home.html', data)

def listagem(request):
    data = {'transactions': Transactions.objects.all()}
    # data['transactions'] = Transactions.objects.filter()
    # data['transactions'] = Transactions.objects.last()
    return render(request, 'account/listagem.html', data)

def new_transaction(request):
    # inicio ao processo
    data = {}
    form = TransactionsForm(request.POST or None)

    if form.is_valid():
        form.send()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'account/form.html', data)

