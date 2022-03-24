from itertools import combinations

LOTTO_SELECT = 6


while True:

    lottoSet = list(map(int,input().split()))

    if lottoSet[0] == 0:
        break

    lottoCombinations = list(combinations(lottoSet[1:],LOTTO_SELECT))
    for combinationsElement in lottoCombinations:
        for element in combinationsElement:
            print(element,end=' ')
        print()
    print()

