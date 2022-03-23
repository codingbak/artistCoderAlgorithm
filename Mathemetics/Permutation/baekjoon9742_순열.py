##permutation 써서 푸는 문제가 아니였다....

from itertools import permutations
import math

while(1):
    try:
        s, stringIdx = map(str, input().split())
    except:
        break

    idx = int(stringIdx)
    sLen = len(s)
    sLenFactorial= math.factorial(sLen)
    result = []
    sList = list(s)
    try :
        while sLen != 0:
            div = sLenFactorial/sLen
            result += sList[int((idx-1)/div)]
            sList.pop(int((idx-1)/div))
            idx -= int((idx-1)/div)*div
            sLen -= 1
            sLenFactorial = div
        print("{} {} = {}".format(s, stringIdx, ''.join(result)))
    except :
        print("{} {} = No permutation".format(s, stringIdx))


