# -*- coding: UTF-8 -*-
#换个格式输出整数
import sys
 
x = raw_input()

if len(x) == 3:
    x1 = (int(x))%10
    x2 = (int(x)/10)%10
    x3 = (int(x)/100)%10 
    a = xrange(1,x1 + 1)
    sys.stdout.write(x3*'B'+x2*'S')
    for i in a:
        sys.stdout.write(str(i)) 
elif len(x) == 2:
    x1 = (int(x))%10
    x2 = (int(x)/10)%10 
    a = xrange(1,x1 + 1)
    sys.stdout.write(x2*'S')
    for i in a:
        sys.stdout.write(str(i)) 
else:
    x1 = (int(x))%10
    a = xrange(1,x1 + 1)
    for i in a:
        sys.stdout.write(str(i))