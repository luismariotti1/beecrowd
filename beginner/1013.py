A, B, C = map(int, input().split())

biggestAB = (A+B+abs(A-B))/2
biggestBC = (B+C+abs(B-C))/2
biggest = (biggestAB+biggestBC+abs(biggestAB-biggestBC))/2

print("{} eh o maior".format(int(biggest)))