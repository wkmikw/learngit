# -*- coding: utf-8 -*-

def lazy_sum(*args):
	def sum():
		ax=0
		for i in args:
			ax=ax+i
		return ax
	return sum

#L=[1,2,3,4,5,6]
f=lazy_sum(1,2,3,4,5,6)

print(f())

# python lazysum.py
