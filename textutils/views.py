# Created by Harsh Gautam

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    dftext = request.GET.get('text', 'default')
    removepunc_res = request.GET.get('removepunc', 'off')
    upper_res = request.GET.get('uppercase', 'off')
    print(dftext)
    print(removepunc_res)
    print(upper_res)
    punctuations = ''',./;:'"[{]}'''
    analyze = ""
    if removepunc_res == 'on':
        if upper_res == 'on':
            dftext = dftext.upper()
        for char in dftext:
            if char not in punctuations:
                analyze += char

        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)
    elif upper_res == 'on':
        analyze = dftext.upper()
        params = {'purpose': 'Uppercase', 'analyzed_text': analyze}
    else:
        params = {'purpose': 'No Purpose', 'analyzed_text': "Select atleast one checkbox!!!"}

    return render(request, 'analyze.html', params)
