from django.shortcuts import render
from .parser import parser_api


def index(request):
    data1 = None
    data_file = None
    if request.method == 'POST':
        if request.POST.get('article'):
            article = request.POST.get('article')
            data1 = parser_api(article)
        if request.FILES.get('file'):
            file = request.FILES.get('file')
            data_file = parser_api(file)

    return render(request, 'main/index.html',{'data1':data1, 'data_file':data_file})

