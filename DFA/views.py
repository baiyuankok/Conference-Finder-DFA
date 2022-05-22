import re
from django.shortcuts import render
from DFA.forms import DFAForm

def indexView(request):
    return render(request, 'index.html')

def state0(input):
    if (input == 'i'):
        state = 1
    elif (input == 'e'):
        state = 40
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
        state = 25
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
        state = 26
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
    elif (input == 'n'):
        state = 4
    elif (input == 'i'):
        state = 22
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
        if (input == 'e'):
            state = 24
        else:
            state = 100  
    return state


def state24(input):
    if(input):
        state = 100
    return state


def state25(input):
    if (input == 'a'):
        state = 26
    elif (input == 'p'):
        state = 29
    elif (input == 'i'):
        state = 31
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
    if (input == 's'):
        state = 28
    else:
        state = 100
    return state


def state28(input):
    if (input):
        state = 100
    return state


def state29(input):
    if (input == 'm'):
        state = 30
    else:
        state = 100
    return state


def state30(input):
    if (input):
        state = 100
    return state


def state31(input):
    if (input == 'm'):
        state = 32
    elif (input == 'r'):
        state = 37
    else:
        state = 100
    return state


def state32(input):
    if (input == 'l'):
        state = 33
    else:
        state = 100
    return state


def state33(input):
    if (input == 'b'):
        state = 34
    else:
        state = 100
    return state


def state34(input):
    if (input == 'd'):
        state = 35
    else:
        state = 100
    return state


def state35(input):
    if (input == 'e'):
        state = 36
    else:
        state = 100
    return state


def state36(input):
    if (input):
        state = 100
    return state


def state37(input):
    if (input == 'm'):
        state = 38
    else:
        state = 100
    return state


def state38(input):
    if (input == 'e'):
        state = 39
    else:
        state = 100
    return state


def state39(input):
    if (input):
        state = 100
    return state


def state40(input):
    if (input == 'u'):
        state = 41
    else:
        state = 100
    return state


def state41(input):
    if (input == 'i'):
        state = 42
    elif (input == 'c'):
        state = 54
    else:
        state = 100
    return state


def state42(input):
    if (input == 'c'):
        state = 43
    elif (input == 'w'):
        state = 50
    else:
        state = 100
    return state


def state43(input):
    if (input == 'n'):
        state = 44
    elif (input == '3'):
        state = 46
    else:
        state = 100
    return state


def state44(input):
    if (input == 'b'):
        state = 45
    else:
        state = 100
    return state


def state45(input):
    if (input):
        state = 100
    return state


def state46(input):
    if (input == 'b'):
        state = 47
    else:
        state = 100
    return state


def state47(input):
    if (input == 'c'):
        state = 48
    else:
        state = 100
    return state


def state49(input):
    if (input):
        state = 100
    return state


def state50(input):
    if (input == 'n'):
        state = 51
    else:
        state = 100
    return state


def state51(input):
    if (input == 'm'):
        state = 52
    else:
        state = 100
    return state


def state52(input):
    if (input == 'c'):
        state = 53
    else:
        state = 100
    return state


def state53(input):
    if (input):
        state = 100
    return state


def state54(input):
    if (input == 'e'):
        state = 55
    else:
        state = 100
    return state


def state55(input):
    if (input == 'l'):
        state = 56
    else:
        state = 100
    return state


def state56(input):
    if (input == 's'):
        state = 57
    else:
        state = 100
    return state


def state57(input):
    if (input):
        state = 100
    return state


def state100(input): # trap state
    if(input):
        state = 100
    return state


def split(string):
    return string.split(" ")


def processDFA(request):
    form = DFAForm(request.POST or None)
    result = ""
    if request.method == "POST":
        form = DFAForm(request.POST)
        if form.is_valid():
            textStringsData = list(form.cleaned_data.GET['testStringsField'])

            finalOutput = list()
            outputDict = dict()
            # Preprocessing the strings
            for lines in textStringsData:
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

                acceptStates = [5, 14, 16, 19, 21, 23, 24, 28, 30, 36, 39, 45, 49, 53, 57]

                for word in flattenedList:
                    currentState = 0
                    for char in word:
                        char = char.casefold()
                        if(re.match(r'[~`!@#$%^&()_={}[\]:;,.<>+\/?-]', char) and (currentState == 0 or currentState in acceptStates)):
                            continue

                        # DFA starts here
                        currentState = locals()['state' + str(currentState)]()

                    if (currentState in acceptStates):
                        matchedGroup = re.match(
                            r'(|[~`!@#$%^&()_={}[\]:;,.<>+\/?-]+)(\w+)(|[ ~`!@#$%^&()_={}[\]:;,.<>+\/?-]+)', word)
                        matchedWord = matchedGroup.group(2) # group 2 to get the word without any other special characters
                        tempWord = re.sub(r'[^\w]', ' ', word).strip().casefold()

                        stats = {
                            'num': 0,
                        }

                        if (outputDict.get(tempWord) is None):
                            outputDict[tempWord] = stats
                        outputDict[tempWord]['num'] += 1
                        index = word.find(matchedWord)
                        word = word[:index] + '<b>' + word[index:index +
                                                        len(matchedWord)] + '</b>' + word[index+len(matchedWord):]
                    tempList.append(word)
                tempString = " ".join(tempList)
                finalOutput.append(tempString)
            finalOutput = " ".join(finalOutput)
            # return finalOutput, outputDict
        else:
            msg = "Please provide input string"
    else:
        form = DFAForm()

    context = {
        "form": form,
        'msg': msg,
        'result': finalOutput
    }
    
    return render(request, 'index.html', context)


# Main code
# def dfa_api(data):
#     splitData = data.split('\n')
#     splitData = [data + "\n" for data in splitData]
#     finalOutput, outputDict = processDFA(splitData)
#     # writeFile(finalOutput, outputDict, len(outputDict))
#     return True