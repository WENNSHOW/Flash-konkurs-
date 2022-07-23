f=open('17.2.txt').readlines()
sp=[int(x) for x in f]
sp1=[x for x in sp if x%15==0]
srar=sum(sp1)//len(sp1)

k=0
mx=-1

for i in range(len(sp)-1):
	for j in range(i+1,len(sp)):
		sm=sp[i]+sp[j]
		if sm%2==0 and sm%17==0 and sm>srar:
			k+=1
			mx=max(mx,sm)
print(k,mx)
