#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

n = int(input())

d = 2
while d * d < n and n % d != 0:
    d += 1  # less efficient

##d = 2
##if n % d != 0:  # if odd
##    d = 3
##    while d * d <= n and n % d != 0:
##        d += 2  # more efficient

if n % d == 0 and n != d:  # in fact, 2 % 2 == 0
    print("The number is divisible by", d)
else:
    print("The number is prime")


'''
Proof. Eratosthenes. Since n is composite, n = d*e
for some natural numbers d and e (both >= 2, d <= e).
If d > sqrt(n) => n = d*e > sqrt(n)*sqrt(n) = n,
i.e. n>n (contraddiction!). So d <= sqrt(n).
'''
