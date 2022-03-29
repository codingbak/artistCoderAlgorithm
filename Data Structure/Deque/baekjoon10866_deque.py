import sys
import copy
input = sys.stdin.readline


def dequePushFront(dequeList, element):
    newList = [element] + dequeList[:]
    return newList

def dequePushBack(dequeList, element):
    dequeList.append(element)
    return

def dequepopFront(dequeList):
    if len(dequeList) == 0:
        return -1
    else:
        return dequeList.pop(0)

def dequepopBack(dequeList):
    if len(dequeList) == 0:
        return -1
    else:
        return dequeList.pop()

def dequeSize(dequeList):
    return len(dequeList)

def dequeEmpty(dequeList):
    if len(dequeList) == 0:
        return 1
    else:
        return 0

def dequeFront(dequeList):
    if len(dequeList) == 0:
        return -1
    else:
        return dequeList[0]

def dequeBack(dequeList):
    if len(dequeList) == 0:
        return -1
    else:
         return dequeList[-1]


queueCommendNumber = int(input())

dequeList = []

for i in range(queueCommendNumber):
    command = input().strip()
    if command == 'pop_front':
        print(dequepopFront(dequeList))

    elif command == 'pop_back':
        print(dequepopBack(dequeList))

    elif command == 'size':
        print(dequeSize(dequeList))

    elif command == 'empty':
        print(dequeEmpty(dequeList))

    elif command == 'front':
        dequeFrontData = dequeFront(dequeList)
        if dequeFrontData == -1:
            print(-1)
        else:
            print(dequeFrontData)

    elif command == 'back':
        dequeBackData = dequeBack(dequeList)
        if dequeBackData == -1:
            print(-1)
        else:
            print(dequeBackData)

    else:
        command , element = map(str, command.split())
        if command[5] == 'f':
            dequeList = copy.deepcopy(dequePushFront(dequeList, element))
        else:
            dequePushBack(dequeList, element)
