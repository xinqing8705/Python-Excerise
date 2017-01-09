# -*- coding:utf-8 -*-
# 函数也是一个对象，而且函数对象能赋值给变量，通过变量来调用
def now():
    print('2017-01-01')

f=now()
f()--->2017-01-01

now.__name__------>'now'
f.__name__------>'now'

#假设我们要增强now()的功能，比如在函数调用前后自动打印日志，但是又不去修改Now()的定义，这就是装饰器decorator

def log(func):
    def wrapper(*args,**kw):
	    print('call %s():'% func.__name__)
		return func(*args,**kw)
	return wrapper
	
@log
#把@log放到now()函数定义处，相当于执行了now=log(now),log()是个装饰器，返回的是一个函数，所以原来的函数仍然存在，
#只是现在同名的now变量指向了新的函数，所以调用Now()会执行新函数，也就是在Log()函数中返回的wrapper()函数
#wapper()的参数定义是（*args,**kw）,wapper()函数可以接受任意参数的调用。
#在wapper()函数内，首先打印日志，然后调用原始的函数。
def now():
    print('2017-01-01')

now()-------->cal now(): 2017-01-01


#如果decorator需要传入参数，那么需要编写一个返回decorator的高阶函数。
def log(text):
    def decorator(func):
        def wapper(*args,**kw):
		    print('%s %s():'%(text,func.__name__))
			return func(*args,**kw)
		return wapper
	return decorator
	
@log('execute')#首先执行log('execute'),返回的是decorator函数，
#再调用返回的参数，参数是now()函数，返回值最终是wrapper函数
def now():
    print('2017-01-01')
	
now()----->execute now():2017-01-01


#一个完整的decorator的写法：
import functools

def log(func):
    @functools.wraps(func)
	def wrapper(*args,**kw):
	    print('call %s():' % func.__name__)
        return func(*args,**kw)
	return wrapper
	
	
	
#带参数的decorator
import functools
def log(text):
    def decorator(func):
	    @functools.wraps(func)
		def wrapper(*args,**kw):
		    print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

	
	
	
	
#能否写出一个@log的decorator，使它既支持：

#@log
#def f():
#   pass
#又支持：

#@log('execute')
#def f():
#    pass

