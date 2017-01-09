# coding = utf-8
# using coding:utf-8 to avoid the charcter acceptance error.
# 用filter求素数
def _odd_iter():#首先定义一个奇数数列
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):#定义一个筛选函数
    return lambda x: x%n>0

def primes():#定义一个生成器
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)#返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it)


# 打印1000以内的素数
for n in primes():
    if n<1000:
        print(n)
    else:
        break
		
		
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
# -*- coding: utf-8 -*-
def is_palindrome(n):
    z=0
    for i in range(len(str(n))//2):
        if str(n)[i]==str(n)[-1-i]:
            z=z+1
			return z==len(str(n))//2
        else: 
            break
			
output=filter(is_palindrome,range(1,1000))
print(list(output))	

		
second way:
def is_palindrome(n):
    a=list(str(n))
	b=list(str(n))
	b.reverse()
	return a==b

output=filter(is_palindrome,range(1,1000))
print(list(output))