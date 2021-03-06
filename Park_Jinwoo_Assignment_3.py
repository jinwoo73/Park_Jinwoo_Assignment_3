#Jinwoo Park
#Kevin Markley
#CSE 1321L section12
import math

#PhoneBill

A = int(input("Account number: "))
S = str(input("Service Type: "))
if  (S == "r" or S == "R"):
    B = int(input("Total minutes: "))
    if (B <= 50):
        print("Amount due: $15.00 ")
    else:
        cost = 15.00 + (B-50)* 0.50
        print ("Amount due: $ ", cost)
else:
    D = int(input("Daytime minutes: "))
    N = int(input("Nighttime minutes: "))
    if (D <= 50 and N <= 100):
        print ("Amount due: $25.00 ")
    elif (D > 50 and N <= 100):
        cost = 25.00 + (D-50) * 0.20
        print ("Amount due: $ ", cost)
    elif (D <= 50 and N > 100):
        cost = 25.00 + (N - 100) * 0.10
        print ("Amount due: $ ", cost)
    else:
        cost = 25.00 + (D-50) * 0.20 + (N - 100) * 0.10
        print ("Amount due: $" ,  cost)


#BestDeal

A = int(input("Small box weight: "))
B = int(input("Small box price: "))
C = int(input("Large box weight: "))
D = int(input("Large box price: "))

if (A/B) < (C/D):
    print ("Judgement: The large box is a better deal")
elif (A/B) == (C/D):
    print ("Judgement: Both boxes are of the same value ")
else:
    print ("Judgement: The smaller box is a better deal ")

#Circles


x1 = int(input("What is the x-coordinate of circle 1?"))
y1 = int(input("What is the y-coordinate of circle 1?"))
r1 = int(input("What is the radius of circle 1?"))
x2 = int(input("What is the x-coordinate of circle 2?"))
y2 = int(input("What is the y-coordinate of circle 2?"))
r2 = int(input("what is the radius of circle 2?"))

print ("Circle 1 center is: ", (x1, y1))
print ("Circle 1 radius is: ", r1)
print ("Circle 2 center is: ", (x2, y2))
print ("Circle 2 radius is: ", r2)

D = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if (D >= r1 + r2):
    print ("Judgement: Circle 2 is completely outside circle 1. ")
elif (D <= abs(r1 - r2)):
    print ("Judgement: Circle 2 completely inside circle 1.")
else:
    print("Judgement: Circle 2 is overlapping with circle 1.")

#IncomeTax

A = int(input("Annual Income: $"))
if (A <= 50000):
    print ("Tax Bracket: 5%")
    print ("Tax due amount: $ " ,A * 0.05 )
elif (50000 < A and A <= 200000):
     print ("Tax Bracket: 10%")
     print ("Tax due amount: $ " ,(2500 + (A-50000) * 0.10))
elif (200000 < A and A <= 400000):
     print ("Tax Bracket: 15%")
     print ("Tax due amount: $ " ,(17500 + (A -200000) * 0.15 ))
elif (400000 < A and A <= 900000):
     print ("Tax Bracket: 25%")
     print ("Tax due amount: $ " ,(47500 + (A - 400000 )*0.25))
else:
     print ("Tax Bracket: 35%")
     print ("Tax due amount: $ " ,(172500 + (A - 900000) * 0.35))

#FiveDigitPalindrom

N = int(input("Entered number: "))
if (N >= 11111 and N <= 99999):
    A = N // 10000
    B = (N - 10000 * A)//1000
    C = (N - 10000 * A - 1000 * B)//100
    D = (N -10000 * A - 1000 * B - 100 * C)//10 
    E = N % 10
    if (A == E and B == D):
        print ("Judgement: valid 5-digit palindrome")
    else:
        print ("Judgement: Invalid 5-digit palindrome")
else:
    print("Judgement: Invalid 5-digit number. Try again")