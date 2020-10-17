# Created by Harsh Gautam

from django.http import HttpResponse
from django.shortcuts import render
from textutils import funcs

def index(request):
    return render(request, 'index.html')

def analyze(request):
    dftext = request.POST.get('text', 'default')
    print(dftext)
    removepunc_res = request.POST.get('removepunc', 'off')
    uppercase_res = request.POST.get('uppercase', 'off')
    removespace_res = request.POST.get('removespace', 'off')
    charcount_res = request.POST.get('charcount', 'off')
    purpose = ""

    try:
        if removepunc_res == 'on':
            analyze = funcs.removepunc(dftext)
            dftext = analyze
            purpose += "Remove Punctuations, "
            # params = {'purpose':'Remove Punctuations', 'analyzed_text': analyze}
        if uppercase_res == 'on':
            analyze = funcs.toUpper(dftext)
            dftext = analyze
            purpose += "Uppercase, "
            # params = {'purpose':'Uppercase', 'analyzed_text': analyze}
        if removespace_res == 'on':
            analyze = funcs.removespaces(dftext)
            dftext = analyze
            purpose += "Remove Extra Spaces, "
            # params = {'purpose':'Remove Extra Spaces', 'analyzed_text': analyze}

        if charcount_res == 'on':
            analyze = funcs.charcount(dftext)
            dftext += "\n\n" + analyze
            purpose += "Character Count, "
            # params = {'purpose':'Character Count', 'analyzed_text': analyze}
        params = {'purpose': purpose, 'analyzed_text': dftext}
    except:
        params = {'purpose': '', 'analyzed_text': "Select atleast one checkbox!!!"}

    return render(request, 'analyze.html', params)
