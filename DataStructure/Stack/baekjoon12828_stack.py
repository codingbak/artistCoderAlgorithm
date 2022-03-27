import sys

input = sys.stdin.readline

def stackPush(stackList, element):
    stackList.append(element)
    return stackList

def stackTop(stackList):
    if len(stackList) ==0:
        return -1
    else:
        return stackList[-1]

def stackSize(stackList):
    return len(stackList)

def stackEmpty(stackList):
    if len(stackList) == 0:
        return 1
    else:
        return 0

def stackPop(stackList):
    if len(stackList) == 0:
        return -1
    else:
        popData = stackList.pop()
        return popData

stackCommendNumber = int(input())

stackList = []
for i in range(stackCommendNumber):
    command = input().strip()

    if command == "top":
        if stackTop(stackList) == -1:
            print(-1)
        else:
            print(stackTop(stackList))

    elif command == "size":
        print(stackSize(stackList))

    elif command == "empty":
        print(stackEmpty(stackList))

    elif command == "pop":
        print(stackPop(stackList))

    else:
        command, element = map(str, command.split())
        element = int(element)
        stackPush(stackList, element)



