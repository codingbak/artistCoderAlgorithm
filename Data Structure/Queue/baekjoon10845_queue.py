import sys

input = sys.stdin.readline

def queuePush(queueList, element):
    queueList.append(element)
    return queueList

def queueBack(queueList):
    if len(queueList) ==0:
        return -1
    else:
        return queueList[-1]

def queueFront(queueList):
    if len(queueList) == 0:
        return -1
    else:
        return queueList[0]

def queueSize(queueList):
    return len(queueList)

def queueEmpty(queueList):
    if len(queueList) == 0:
        return 1
    else:
        return 0

def queuePop(queueList):
    if len(queueList) == 0:
        return -1
    else:
        popData = queueList.pop(0)
        return popData

queueCommendNumber = int(input())

queueList = []
for i in range(queueCommendNumber):
    command = input().strip()

    if command == "front":
        if queueFront(queueList) == -1:
            print(-1)
        else:
            print(queueFront(queueList))

    elif command == "back":
        if queueBack(queueList) == -1:
            print(-1)
        else:
            print(queueBack(queueList))

    elif command == "size":
        print(queueSize(queueList))

    elif command == "empty":
        print(queueEmpty(queueList))

    elif command == "pop":
        print(queuePop(queueList))

    else:
        command, element = map(str, command.split())
        element = int(element)
        queuePush(queueList, element)



