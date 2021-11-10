from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .models import NameForm, Logs


def log_list(request):
    domain_name = 'https://gooogle.com'
    log_text = '123 qwe zxc poi'
    return render(request, 'logs/logs_list.html', {'domain_name': domain_name, 'log_text': log_text})
@csrf_exempt
def result(request):
    dom_name = request.GET['domain']
    loges = request.GET['logs']
    # Logs.objects.create(domain=dom_name, text_log=loges, date_add='2021-11-09')
    logs_logs = Logs.objects.filter(domain='https://gooogle.com').values()
    return render(request, 'logs/result.html', {'domain': dom_name, 'logs': loges, 'bd': logs_logs})
    # if request.method == 'POST':
    #     form = NameForm(request.POST)
    #     if form.is_valid():
    #         ar1 = form.META
    #
    #     return render(request, 'logs/result.html', {'res': ar1})
    # elif request.method == 'GET':
    #     keys = []
    #     for key in request.GET:
    #         keys.append(key)

    # return render(request, 'logs/result.html', {'res': res})
# Create your views here.
