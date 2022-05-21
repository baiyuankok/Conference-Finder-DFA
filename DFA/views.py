import re
from django.shortcuts import render

def indexView(request):
    return render(request, 'index.html')

# This function is for the dfa = starting
# dfa = state (zeroth) of DFA
def start(input):
    if (input == 'i'):
        state = 1
    else:
        state = 100 # state 100 serves as the trap state
    return state


def state1(input):
    if (input == 'c'):
        state = 2
    else:
        state = 100
    return state


def state2(input):
    if (input == 'm'):
        state = 3
    elif (input == 'i'):
        state = 6
    elif (input == 'b'):
        state = 9
    elif (input == 'e'):
        state = 11
    elif (input == 'c'):
        state = 17
    elif (input == 'a'):
        state = 24
    else:
        state = 100
    return state


def state3(input):
    if(input == 'b'):
        state = 4
    else:
        state = 100
    return state


def state4(input):
    if (input == 's'):
        state = 5
    else:
        state = 100
    return state


def state5(input):
    if(input):
        state = 100
    return state


def state6(input):
    if (input == 't'):
        state = 4
    elif (input == 'r'):
        state = 7
    else:
        state = 100
    return state


def state7(input):
    if (input == 'p'):
        state = 8
    else:
        state = 100
    return state


def state8(input):
    if (input == 'e'):
        state = 3
    else:
        state = 100
    return state


def state9(input):
    if (input == 'a'):
        state = 10
    elif (input == 'm'):
        state = 25
    else:
        state = 100
    return state


def state10(input):
    if (input == 'e'):
        state = 4
    else:
        state = 100
    return state


def state11(input):
    if (input == 'a'):
        state = 12
    elif (input == 'f'):
        state = 15
    else:
        state = 100
    return state


def state12(input):
    if (input == 'b'):
        state = 13
    else:
        state = 100
    return state


def state13(input):
    if (input == 't'):
        state = 14
    else:
        state = 100
    return state


def state14(input):
    if(input):
        state = 100
    return state


def state15(input):
    if (input == 'r'):
        state = 16
    else:
        state = 100
    return state


def state16(input):
    if(input):
        state = 100
    return state


def state17(input):
    if (input == 's'):
        state = 18
    elif (input == 'b'):
        state = 22
    else:
        state = 100
    return state


def state18(input):
    if (input == 'p'):
        state = 19
    else:
        state = 100
    return state


def state19(input):
    if (input):
        if (input == 'e'):
            state = 20
        else:
            state = 100  
    return state


def state20(input):
    if (input == 'e'):
        state = 21
    else:
        state = 100
    return state


def state21(input):
    if(input):
        state = 100
    return state


def state22(input):
    if (input == 'e'):
        state = 23
    else:
        state = 100
    return state


def state23(input):
    if (input):
        state = 100
    return state


def state24(input):
    if (input == 'a'):
        state = 25
    elif (input == 'p'):
        state = 28
    elif (input == 'i'):
        state = 30
    else:
        state = 100
    return state


def state25(input):
    if (input == 's'):
        state = 26
    else:
        state = 100
    return state


def state26(input):
    if (input == 's'):
        state = 27
    else:
        state = 100
    return state


def state27(input):
    if (input):
        state = 100
    return state


def state28(input):
    if (input == 'm'):
        state = 29
    else:
        state = 100
    return state


def state29(input):
    if (input):
        state = 100
    return state


def state30(input):
    if (input == 'm'):
        state = 31
    elif (input == 'r'):
        state = 36
    else:
        state = 100
    return state


def state31(input):
    if (input == 'l'):
        state = 32
    else:
        state = 100
    return state


def state32(input):
    if (input == 'b'):
        state = 33
    else:
        state = 100
    return state


def state33(input):
    if (input == 'd'):
        state = 34
    else:
        state = 100
    return state


def state34(input):
    if (input == 'e'):
        state = 35
    else:
        state = 100
    return state


def state35(input):
    if (input):
        state = 100
    return state


def state36(input):
    if (input == 'm'):
        state = 37
    else:
        state = 100
    return state


def state37(input):
    if (input == 'e'):
        state = 38
    else:
        state = 100
    return state


def state38(input):
    if (input):
        state = 100
    return state


def state100(input): # trap state
    if(input):
        state = 100
    return state


def split(string):
    return string.split(" ")


def processDFA(data):
    finalOutput = list()
    outputDict = dict()
    # Preprocessing the strings
    for lines in data:
        # split string into list by whitespace
        line = lines.split(" ")
        # separate the newline character from words with whitespace
        # and
        # split the separated string into list by whitespace
        line = [split(i[:-1] + " " + i[-1:])
                if re.match(r'([^\s]+)\n', i) else i for i in line]
        flattenedList = []
        # flatten the list if found nested list
        for i in line:
            if isinstance(i, list):
                for item in i:
                    flattenedList.append(item)
            else:
                flattenedList.append(i)

        tempList = list()

        acceptStates = [5, 14, 16, 19, 21, 23, 27, 29, 35, 38]

        for word in flattenedList:
            currentState = 0
            for char in word:
                char = char.casefold()
                if(re.match(r'[~`!@#$%^&()_={}[\]:;,.<>+\/?-]', char) and (currentState == 0 or currentState in acceptStates)):
                    continue

                # DFA starts here
                if (currentState == 0):
                    currentState = start(char)
                elif (currentState == 1):
                    currentState = state1(char)
                elif (currentState == 2):
                    currentState = state2(char)
                elif (currentState == 3):
                    currentState = state3(char)
                elif (currentState == 4):
                    currentState = state4(char)
                elif (currentState == 5):
                    currentState = state5(char)
                elif (currentState == 6):
                    currentState = state6(char)
                elif (currentState == 7):
                    currentState = state7(char)
                elif (currentState == 8):
                    currentState = state8(char)
                elif (currentState == 9):
                    currentState = state9(char)
                elif (currentState == 10):
                    currentState = state10(char)
                elif (currentState == 11):
                    currentState = state11(char)
                elif (currentState == 12):
                    currentState = state12(char)
                elif (currentState == 13):
                    currentState = state13(char)
                elif (currentState == 14):
                    currentState = state14(char)
                elif (currentState == 15):
                    currentState = state15(char)
                elif (currentState == 16):
                    currentState = state16(char)
                elif (currentState == 17):
                    currentState = state17(char)
                elif (currentState == 18):
                    currentState = state18(char)
                elif (currentState == 19):
                    currentState = state19(char)
                elif (currentState == 20):
                    currentState = state20(char)
                elif (currentState == 21):
                    currentState = state21(char)
                elif (currentState == 22):
                    currentState = state22(char)
                elif (currentState == 23):
                    currentState = state23(char)
                elif (currentState == 24):
                    currentState = state24(char)
                elif (currentState == 25):
                    currentState = state25(char)
                elif (currentState == 26):
                    currentState = state26(char)
                elif (currentState == 27):
                    currentState = state27(char)
                elif (currentState == 28):
                    currentState = state28(char)
                elif (currentState == 29):
                    currentState = state29(char)
                elif (currentState == 30):
                    currentState = state30(char)
                elif (currentState == 31):
                    currentState = state31(char)
                elif (currentState == 32):
                    currentState = state32(char)
                elif (currentState == 33):
                    currentState = state33(char)
                elif (currentState == 34):
                    currentState = state34(char)
                elif (currentState == 35):
                    currentState = state35(char)
                elif (currentState == 36):
                    currentState = state36(char)
                elif (currentState == 37):
                    currentState = state37(char)
                elif (currentState == 38):
                    currentState = state38(char)
                elif (currentState == 100):
                    currentState = state100(char)

            coorConj = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']

            if (currentState in acceptStates):
                matchedGroup = re.match(
                    r'(|[~`!@#$%^&()_={}[\]:;,.<>+\/?-]+)(\w+)(|[ ~`!@#$%^&()_={}[\]:;,.<>+\/?-]+)', word)
                matchedWord = matchedGroup.group(2)
                tempWord = re.sub(r'[^\w]', ' ', word).strip().casefold()

                stats = {
                    'num': 0,
                    'type': ''
                }

                if (outputDict.get(tempWord) is None):
                    outputDict[tempWord] = stats
                outputDict[tempWord]['num'] += 1
                if(tempWord in coorConj):
                    outputDict[tempWord]['type'] = 'Coordinating Conjunction'
                else:
                    outputDict[tempWord]['type'] = 'Subcoordinating Conjunction'
                index = word.find(matchedWord)
                word = word[:index] + '<b>' + word[index:index +
                                                   len(matchedWord)] + '</b>' + word[index+len(matchedWord):]
            tempList.append(word)
        tempString = " ".join(tempList)
        finalOutput.append(tempString)
    finalOutput = " ".join(finalOutput)
    return finalOutput, outputDict


# Main code
def dfa_api(data):
    splitData = data.split('\n')
    splitData = [data + "\n" for data in splitData]
    finalOutput, outputDict = processDFA(splitData)
    # writeFile(finalOutput, outputDict, len(outputDict))
    return True