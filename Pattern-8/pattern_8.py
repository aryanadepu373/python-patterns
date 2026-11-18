n=int(input("Enter:"))
count=1;
for i in range(n):
	if(i==0):
		print(" "*(n-i-1)+"*")
	elif(i==n-1):
		print("*"*((2*n)-1))
	else:
		print(" "*(n-i-1)+"*"+" "*count+"*")
		count=count+2;
		
count=count-2;
for i in range(n-1):
	if(i==n-2):
		print(" "*(i+1)+"*")
	else:
		print(" "*(i+1)+"*"+" "*count+"*")
		count=count-2;

