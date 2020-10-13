# Created by Harsh Gautam

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    dftext = request.GET.get('text', 'default')
    choice = request.GET.get('choice', 'off')
    analyze = ""
    if choice == 'removepunc':
        punctuations = '''"<!@#$%^&*()][}{;'.,/:?>'''
        for char in dftext:
            if char not in punctuations:
                analyze += char
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyze}
    elif choice == 'uppercase':
        analyze = dftext.upper()
        params = {'purpose': 'Uppercase', 'analyzed_text': analyze}
    elif choice == 'removespace':
        for index, char in enumerate(dftext):
            if dftext[index] == ' ' and dftext[index+1] == ' ':
                pass
            else:
                analyze += char
        params = {'purpose': "Remove Extra Spaces", 'analyzed_text': analyze}
    elif choice == 'charcount':
            dftext_len = len(dftext)
            char_count = {key: 0 for key in tuple(dftext)}
            for char in dftext:
                char_count[char] += 1
            analyze = analyze + "Total Characters: " + str(dftext_len) + "\n Characters Count: " +  str(char_count)
            params = {'purpose': "Counting Characters", 'analyzed_text': analyze}
    else:
        params = {'purpose': 'No Purpose', 'analyzed_text': "Select atleast one checkbox!!!"}

    return render(request, 'analyze.html', params)
