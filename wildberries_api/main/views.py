import pandas

from django.shortcuts import render

from .parser import parser_csr


def index(request):
    if request.method == 'POST':
        if request.POST.get('article'):
            article = request.POST.get('article')
            print(article)
            parser_csr(article)
        if request.FILES.get('file'):
            file = request.FILES.get('file')
            print(file)
    return render(request, 'main/index.html')

