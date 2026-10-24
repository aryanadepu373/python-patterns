n=int(input("Enter:"))
for i in range(n):
	k=1;
	for j in range(i+1):
		if(j%2==0):
			print(k,end="")
			k=k+1
		else:
			print(" * ",end="")
	print()
