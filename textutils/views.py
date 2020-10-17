# Created by Harsh Gautam

from django.http import HttpResponse
from django.shortcuts import render
from textutils import funcs # funcs.py that has various functions for text analyzer

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text from textarea
    dftext = request.POST.get('text', 'default')
    
    # Get values for various sqwitches/checkboxes
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
            
        if uppercase_res == 'on':
            analyze = funcs.toUpper(dftext)
            dftext = analyze
            purpose += "Uppercase, "
            
        if removespace_res == 'on':
            analyze = funcs.removespaces(dftext)
            dftext = analyze
            purpose += "Remove Extra Spaces, "

        if charcount_res == 'on':
            analyze = funcs.charcount(dftext)
            dftext += "\n\n" + analyze
            purpose += "Character Count, "
            
        params = {'purpose': purpose, 'analyzed_text': dftext}
    except:
        params = {'purpose': '', 'analyzed_text': "Select atleast one checkbox!!!"}

    return render(request, 'analyze.html', params)
