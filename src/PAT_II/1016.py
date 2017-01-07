# -*- coding: UTF-8 -*-
'''
正整数A的“DA（为1位整数）部分”定义为由A中所有DA组成的新整数PA。
例如：给定A = 3862767，DA = 6，则A的“6部分”PA是66，因为A中有2个6。

现给定A、DA、B、DB，请编写程序计算PA + PB。

输入格式：

输入在一行中依次给出A、DA、B、DB，中间以空格分隔，其中0 < A, B < 1010。

输出格式：

在一行中输出PA + PB的值。

输入样例1：
3862767 6 13530293 3
输出样例1：
399
输入样例2：
3862767 1 13530293 8
输出样例2：
0
'''  
import re

A = []
B = []
DA = []
DB = []
s = 0
w = 0
i = 1
r = 1

A,DA,B,DB = raw_input().strip().split()

for x in re.findall(DA,A):
    s = s + int(x) * (10 ** (i - 1))
    i = i + 1
    
for y in re.findall(DB,B):
    w = w + int(y) * (10 ** (r - 1))
    r = r + 1 
    
print s + w



