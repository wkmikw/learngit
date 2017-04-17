# -*- coding: utf-8 -*-
#杨辉三角generator

#扩展下一行
def ex1(a1):
	i=0
	a2=[]
	l=len(a1)
	while i<l:
		if i==0:
			a2.append(1)
		else:
			a2.append(a1[i-1]+a1[i])
		i=i+1
	a2.append(1)
	return a2

#generator
def triangles():
	L=[]
	L.append(1)
	while True:
		yield L
		L=ex1(L)
	return
#output
n=1
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

# python yield.py