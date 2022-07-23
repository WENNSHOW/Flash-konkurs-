# 1 способ
f=open('17.txt').readlines()
sp=[int(x) for x in f]
sp1=[x for x in sp if 999<x<10000]
sp2=[x for x in sp1 if int(str(x)[1])%2!=0]
print(len(sp2),sum(sp2))

# 2 способ
f=open('17.txt').readlines()
sp=[int(x) for x in f]
sp1=[]
for i in range(len(sp)):
	x=sp[i]
	if 999<x<10000 and int(str(x)[1])%2!=0:
		sp1.append(x)
print(len(sp1),sum(sp1))