n=int(input("Enter:"))
for i in range(n):
	print(" "*i+"* "*(n-i))
print(" "*(n-1)+"* ")
for i in range(n):
	print(" "*(n-i-1)+"* "*(i+1))
	
