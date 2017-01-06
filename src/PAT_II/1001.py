# -*- coding: UTF-8 -*-  
def f(x):
    if x % 2 == 0:
        x = x/2
    else:
        x = (3*x + 1)/2
    return x 

n = input()
i = 0

if n == 1:
    print 1
else:
    while(n != 1):
        n = f(n)
        i = i + 1
    print i
    