#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

# define variables a and b
a = 10
b = 5

# perform mathematical operations using the imported functions
sum_result = add(a, b)
diff_result = sub(a, b)
prod_result = mul(a, b)
quo_result = div(a, b)

# print the results using string format
print("{0} + {1} = {2}".format(a, b, sum_result))
print("{0} - {1} = {2}".format(a, b, diff_result))
print("{0} * {1} = {2}".format(a, b, prod_result))
print("{0} / {1} = {2}".format(a, b, quo_result))
