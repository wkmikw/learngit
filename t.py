'''
l=[]
l.append(1)
#print(l)

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

l=[1,2,1]
l=ex1(l)

print(l)

#python t.py

'''

