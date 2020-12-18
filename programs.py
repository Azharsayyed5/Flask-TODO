# Write a program to calculate and print the factorial of a number using a for loop.

num = int(input("enter a number: "))
 
fac = 1
 
for i in range(1, num + 1):
	fac = fac * i
 
print("factorial of ", num, " is ", fac)

# Write a python script to construct the following pattern
# (a) 
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
# (b)
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
                                                             
