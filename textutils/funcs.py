
def removepunc(dftext):
    analyze = ''
    punctuations = '''"<!@#$%^&*()][}{;'.,/:?>'''
    for char in dftext:
        if char not in punctuations:
            analyze += char
    return analyze

def toUpper(dftext):
    analyze = ''
    analyze = dftext.upper()
    return analyze

def removespaces(dftext):
    analyze = ''
    for index, char in enumerate(dftext):
        if dftext[index] == ' ' and dftext[index+1] == ' ':
            pass
        else:
            analyze += char
    return analyze

def charcount(dftext):
    analyze = ''
    dftext_len = len(dftext)
    char_count = {key: 0 for key in tuple(dftext)}
    for char in dftext:
        char_count[char] += 1
    analyze = analyze + "Total Characters: " + str(dftext_len) + "\nCharacters Count: " +  str(char_count)
    return analyze