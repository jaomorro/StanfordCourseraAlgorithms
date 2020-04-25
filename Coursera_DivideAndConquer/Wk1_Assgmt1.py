"""
In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.
To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.
"""

def mult(num1,num2):
    final_product = 0
    zeros = 0
    for i in range(len(str(num2))-1,-1,-1):
        print(f"i = {i}")
        num2_i = int(str(num2)[i])
        product = []
        tens_digit = 0
        for zero in range(zeros):
            product.append('0')
        for j in range(len(str(num1))-1,-1,-1):
            num1_j = int(str(num1)[j])
            print(f"{num2_i} * {num1_j} + {tens_digit}")
            prod = str(num2_i * num1_j + int(tens_digit))
            print(f"prod = {prod}")
            if len(prod) > 1:
                tens_digit = prod[0]
                product.append(prod[1])
            else:
                product.append(prod[0])
                tens_digit = 0
        if int(tens_digit) > 0:
            product.append(tens_digit)
        product = product[::-1]
        zeros += 1

        product = product[::-1]
        print(f"product = {product}")
        final_product += int(''.join(product)[::-1])

    return final_product

num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627
print(mult(num1,num2))


