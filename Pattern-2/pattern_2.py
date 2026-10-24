n=int(input("Enter:"))
count=0;
for i in range(n):
	if (i==0):
		print(" "*(n-i-1)+"*")
	elif (i==1):
		print(" "*(n-i-1)+"*"+" "+"*")
	else:
		count=(2*i)-3
		print(" "*(n-i-1)+"**"+" "*((2*i)-3)+"**")

for i in range(n-1):
	if (i==n-2):
		print(" "*(i+1)+"*")
	elif (i==n-3):
		print(" "*(i+1)+"*"+" "+"*")
	else:
		count=count-2
		print(" "*(i+1)+"**"+" "*count+"**")
