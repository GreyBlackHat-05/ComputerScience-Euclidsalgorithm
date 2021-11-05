#Euclid's algorithm is a way to find the greatest common divisor of 2 numbers
#Try Entering 8 and 12: The GCD is 4.

A = input("Number A?\n")
B = input("number B?\n")

A = int(A)
B = int(B)


while True:
    if B == 0:
        break

    elif A > B:
        A = A - B
    else:
        B = B - A

print(A)
