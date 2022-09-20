KmL = 12

spentTimeH = int(input())
speedKmH = int(input())

distance = spentTimeH * speedKmH

consumption = distance / KmL

print("{:.3f}".format(consumption))
