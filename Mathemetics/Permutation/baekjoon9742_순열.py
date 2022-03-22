##permutation 써서 푸는 문제가 아니였다....

from itertools import permutations

while(1):
    try:
        s, idx = map(str, input().split())
    except:
        break

    try:
        result = ''.join(list(permutations(s))[int(idx) - 1])
        print("{} {} = {}".format(s, idx, result))
    except:
        print("{} {} = No permutation".format(s, idx))