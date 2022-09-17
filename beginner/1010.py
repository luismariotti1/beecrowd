firstProduct = input()
secondProduct = input()

code1, quantity1, price1 = firstProduct.split()
code2, quantity2, price2 = secondProduct.split()

total = int(quantity1) * float(price1) + int(quantity2) * float(price2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))