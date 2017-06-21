import math
import cmath

a = float(input('please input a:'))
b = float(input('please input b:'))
c = float(input('please input c:'))

d = b**2 - 4*a*c

q1 = (-b - cmath.sqrt(d)) / 2*a
q2 = (-b + cmath.sqrt(d)) / 2*a

print('two answers of equation is {0},{1}'.format(q1,q2))
