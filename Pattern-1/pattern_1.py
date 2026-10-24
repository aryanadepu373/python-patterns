n=int(input("Enter"))
for i in range(n):
	if(i!=n-1):
		print(" "*(n-i)+"*"*((2*i)+1))
	else:
		print("*"*((2*i)+3))
		
for i in range(n-1):
	print(" "*(i+2)+"*"*((2*(n-i))-3))