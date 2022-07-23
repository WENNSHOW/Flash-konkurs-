def alf(a,b):
	al='0123456789ABCDEF'
	o=' '
	while a>0:
		o=al[a%b]+o
		a=a//b	
	return o

f=open('17.3.txt').readlines()
sp=[int(x) for x in f]
sp1=[x for x in sp if x%56==0]
srar=sum(sp1)//len(sp1)
sp128=max([x for x in sp if x%128==0])

k=0
mn=10**1000

for i in range(len(sp)-1):
	for j in range(i+1,len(sp)):
	a=sp[i]
	b=sp[j]
	if ((a>sp128) or (b>sp128)) and (('25' in alf(a,9)) or ('25' in alf(b,9))) and (a+b)>srar:
		k+=1
		mn=min(mn,a+b)
print(k,mn)