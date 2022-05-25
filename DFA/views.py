import re
from django.shortcuts import render
from DFA.forms import DFAForm

def indexView(request):
    form = DFAForm(request.POST or None)
    return render(request, 'index.html', {'form': form})

def state0(input):
    if (input == 'i'):
        state = 1
    elif (input == 'e'):
        state = 40
    else:
        state = 100 # state 100 serves as the trap state
    return state


def splitString(string):
    return string.split(" ")


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


def state48(input):
    if (input == 'b'):
        state = 49
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


# Trap state
def state100(input):
    if(input):
        state = 100
    return state


def processDFA(request):
    form = DFAForm(request.POST or None)
    accepted = False
    processedUserInput = []
    DFAFindings = dict()
    acceptStates = [5, 14, 16, 19, 21, 23, 24, 28, 30, 36, 39, 45, 49, 53, 57]

    if request.method == "POST":
        form = DFAForm(request.POST)
        if form.is_valid():
            startIndex_originalText = 0
            testStringsData = form.cleaned_data['testStrings']

            # Split the line into list and restore the new line character that was split
            lineList = testStringsData.split('\n')
            lineList = [element + "\n" for element in lineList]

            for line in lineList:
                stringList = line.split(" ")

                newStringList = []
                for each in stringList:
                    # Check whether the last two char are '\n'
                    if each[-1:-2:-1] == '\n':
                        newStringList.append(splitString(each[:-1] + " " + each[-1:]))
                    else:
                        newStringList.append(each)

                flatList = []
                for sublist in newStringList:
                    # Check whether the sublist is a list
                    if isinstance(sublist, list):
                        for element in sublist:
                            flatList.append(element)
                    else:
                        flatList.append(sublist)

                wordList = []

                for word in flatList:
                    currentState = 0
                    for char in word:
                        # Change all the char to lower case
                        char = char.casefold()

                        # Skip the DFA traversal if the char is special char or currentState conditions are met
                        regex = re.compile(r'[~`!@#$%^&()_={}[\]:;,.<>+\/?-]')
                        if(regex.search(char) != None and (currentState == 0 or currentState in acceptStates)):
                            continue

                        # DFA traversal on char
                        currentState = eval(('state' + str(currentState)) + "(char)")

                    if (currentState in acceptStates):
                        accepted = True

                        # Group word by following (1-special char) -> (2-strings) -> (3-special char)
                        wordGroup = re.match(r'(|[~`!@#$%^&()_={}[\]:;,.<>+\/?-]+)(\w+)(|[ ~`!@#$%^&()_={}[\]:;,.<>+\/?-]+)', word)
                        
                        # Obtain the word from group 2
                        pureWord = wordGroup.group(2)
                        tempWord = re.sub(r'[^\w]', ' ', word).strip()
                        findings = {
                            'occurenceNum': 0,
                            'position': []
                        }

                        # Create new key if not the word is not in the list
                        if (DFAFindings.get(tempWord) is None):
                            DFAFindings[tempWord] = findings
                            
                        # Assign occurenceNum and index position for each key
                        DFAFindings[tempWord]['occurenceNum'] += 1
                        occurenceIndexPosition = testStringsData.index(tempWord, startIndex_originalText)
                        DFAFindings[tempWord]['position'].append(occurenceIndexPosition)
                        startIndex_originalText = occurenceIndexPosition + 1

                        # Assign boldface on the pattern found
                        indexPosition = word.find(pureWord)
                        word = word[:indexPosition] + '<b>' + word[indexPosition:indexPosition + len(pureWord)] + '</b>' + word[indexPosition+len(pureWord):]

                    # Store each (accepted & rejected) processed word in list
                    wordList.append(word)

                # Convert the list to a string
                wordListText = " ".join(wordList)

                # Store the converted string to list
                processedUserInput.append(wordListText)

            # Convert the list to a string (final output)
            processedUserInput = " ".join(processedUserInput)
    else:
        form = DFAForm()

    context = {
        "form": form,
        'userInput': processedUserInput,
        'output': DFAFindings,
        'accepted': accepted
    }
    
    return render(request, 'result.html', context)