n=int(input("Enter:"))
m=int(input("Enter:"))
val=n//2
if(n%2==0):
	val=val-1
for i in range(n):
	if(i==val):
		print("*"*m)
	else:
		print("*"+" "*(m-2)+"*")
