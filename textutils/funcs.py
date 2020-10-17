# Function to remove punctuations from text
def removepunc(dftext):
    analyze = ''
    punctuations = '''"<!@#$%^&*()][}{;'.,/:?>'''
    for char in dftext:
        if char not in punctuations:
            analyze += char
    return analyze

# Function to convert text to Uppercase
def toUpper(dftext):
    analyze = ''
    analyze = dftext.upper()
    return analyze

# Function to remove extra spaces from the given text
def removespaces(dftext):
    analyze = ''
    for index, char in enumerate(dftext):
        if dftext[index] == ' ' and dftext[index+1] == ' ':
            pass
        else:
            analyze += char
    return analyze

# Funtion to coun the number of characters in text. It couns total characters and each character's count.
def charcount(dftext):
    analyze = ''
    dftext_len = len(dftext)
    char_count = {key: 0 for key in tuple(dftext)} # Dict comprehension for generating dictionary with keys of value 0
    for char in dftext:
        char_count[char] += 1
    analyze = analyze + "Total Characters: " + str(dftext_len) + "\nCharacters Count: " +  str(char_count)
    return analyze