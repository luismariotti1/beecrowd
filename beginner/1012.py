pi = 3.14159

values = input()

A, B, C = values.split()

A = float(A)
B = float(B)
C = float(C)

areaOfTheTriangule = A * C / 2
areaOfTheCircle = pi * pow(C,2)
areaOfTheTrapezium = (A + B) * C / 2
areaOfTheSquare = pow(B,2)
areaOfTheRectangle = A * B


print("TRIANGULO: {:.3f}".format(areaOfTheTriangule))
print("CIRCULO: {:.3f}".format(areaOfTheCircle))
print("TRAPEZIO: {:.3f}".format(areaOfTheTrapezium))
print("QUADRADO: {:.3f}".format(areaOfTheSquare))
print("RETANGULO: {:.3f}".format(areaOfTheRectangle))