n = int(input("Enter the length of the sequence: "))

counter = 0
num1= 1
num2= 2
num3= 3

while counter <= n:
    if counter == 0:
        summa = num1
        print(summa)
    elif counter == 1:
        summa = num1 + 1
        print(summa)
    elif counter == 2:
        summa = num1 + num2
        print(summa)
    else:
        summa = num1 + num2 + num3
        num1= num2
        num2= num3
        num3= summa
        print(summa)
    counter += 1

