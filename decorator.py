# -*- coding:utf-8 -*-
# ����Ҳ��һ�����󣬶��Һ��������ܸ�ֵ��������ͨ������������
def now():
    print('2017-01-01')

f=now()
f()--->2017-01-01

now.__name__------>'now'
f.__name__------>'now'

#��������Ҫ��ǿnow()�Ĺ��ܣ������ں�������ǰ���Զ���ӡ��־�������ֲ�ȥ�޸�Now()�Ķ��壬�����װ����decorator

def log(func):
    def wrapper(*args,**kw):
	    print('call %s():'% func.__name__)
		return func(*args,**kw)
	return wrapper
	
@log
#��@log�ŵ�now()�������崦���൱��ִ����now=log(now),log()�Ǹ�װ���������ص���һ������������ԭ���ĺ�����Ȼ���ڣ�
#ֻ������ͬ����now����ָ�����µĺ��������Ե���Now()��ִ���º�����Ҳ������Log()�����з��ص�wrapper()����
#wapper()�Ĳ��������ǣ�*args,**kw��,wapper()�������Խ�����������ĵ��á�
#��wapper()�����ڣ����ȴ�ӡ��־��Ȼ�����ԭʼ�ĺ�����
def now():
    print('2017-01-01')

now()-------->cal now(): 2017-01-01


#���decorator��Ҫ�����������ô��Ҫ��дһ������decorator�ĸ߽׺�����
def log(text):
    def decorator(func):
        def wapper(*args,**kw):
		    print('%s %s():'%(text,func.__name__))
			return func(*args,**kw)
		return wapper
	return decorator
	
@log('execute')#����ִ��log('execute'),���ص���decorator������
#�ٵ��÷��صĲ�����������now()����������ֵ������wrapper����
def now():
    print('2017-01-01')
	
now()----->execute now():2017-01-01


#һ��������decorator��д����
import functools

def log(func):
    @functools.wraps(func)
	def wrapper(*args,**kw):
	    print('call %s():' % func.__name__)
        return func(*args,**kw)
	return wrapper
	
	
	
#��������decorator
import functools
def log(text):
    def decorator(func):
	    @functools.wraps(func)
		def wrapper(*args,**kw):
		    print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

	
	
	
	
#�ܷ�д��һ��@log��decorator��ʹ����֧�֣�

#@log
#def f():
#   pass
#��֧�֣�

#@log('execute')
#def f():
#    pass

