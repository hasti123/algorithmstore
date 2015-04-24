def runProgram():
    print("Enter the number of values you want to choose from(e.g. 1,2...10)")
    listlength = int(input())
    choices = []
    for i in range(listlength):
        print("Enter a value:")
        temp = input()
        choices.append(temp)

    while(len(choices) > 1):
        choices = narrowdown(choices)

    print(choices)

def narrowdown(choices):
    tempList = []

    if len(choices) % 2 != 0:
          choices.append("") 
    
    for i in range(0,len(choices),2):
        print("1: {0} or 2: {1}".format(choices[i],choices[i+1]))
        choice = int(input())
        if choice == 1:
            tempList.append(choices[i])
        else:
            tempList.append(choices[i+1])
        
    return tempList
