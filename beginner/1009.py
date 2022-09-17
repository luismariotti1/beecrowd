sellerName = input()
sellerFixedSalary = float(input())
sellerSales = float(input())

salary = sellerFixedSalary + sellerSales * 0.15

print("TOTAL = R$ {:.2f}".format(salary))