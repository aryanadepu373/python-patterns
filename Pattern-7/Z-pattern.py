t=int(input())
for i in range(t):
	if(i!=0 and i!=(t-1)):
		print(" "*(t-i-1)+"*")
	else:
		print("*"*t)