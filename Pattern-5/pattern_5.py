n=int(input("Enter:"))
for i in range(n):
	print(" "*(n-i-1),end="")
	k=0;
	for j in range(i+1):
		if(k%2==0):
			print(str(1)+" ",end="")
		elif(k%2!=0):
			print(str(0)+" ",end="")
		k=k+1
	print()