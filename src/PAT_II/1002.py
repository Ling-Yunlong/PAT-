# -*- coding: UTF-8 -*-  

#读入一个自然数n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

#输入格式：每个测试输入包含1个测试用例，即给出自然数n的值。这里保证n小于10100。

#输出格式：在一行内输出n的各位数字之和的每一位，拼音数字间有1 空格，但一行中最后一个拼音数字后没有空格。

#输入样例：
#1234567890987654321123456789
#输出样例：
#yi san wu

n = raw_input()
i = 1
x = []
r = 1
rn = []


while (i <= len(n)):
    x.append((int(n)/(10**(i - 1)))%10)
    i = i + 1

cal_sum = sum(x)


while(r <= len(str(cal_sum))):
    rn.append((cal_sum/(10**(r - 1)))%10)
    r = r + 1
    
rn.reverse()
    
for m in rn:
    if m == 0:
        print 'ling',
    elif m == 1:
        print 'yi',
    elif m == 2:
        print 'er',
    elif m == 3:
        print 'san',
    elif m == 4:
        print 'si',
    elif m == 5:
        print 'wu',
    elif m == 6:
        print 'liu',
    elif m == 7:
        print 'qi',
    elif m == 8:
        print 'ba',
    else:
        print 'jiu',

    
    
    
