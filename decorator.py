# -*- coding: utf-8 -*-
# python decorator.py


import functools

def log(text=''):
	if text:
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('begin call')
				print('%s %s():' % (text, func.__name__))
				func(*args, **kw)
				print('end call')
			return wrapper
		return decorator

	else:
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('begin call')	
				print('%s():' % func.__name__)			
				func(*args, **kw)
				print('end call')
			return wrapper
		return decorator		




@log('JK')
def now():
	print('2015-3-25')

now()

print('\n')

@log()
def now():
	print('2015-3-25')

now()


'''
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
'''