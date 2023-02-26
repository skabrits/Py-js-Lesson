import time

a = int(input('enter num >'))
max = a
while a > 0:
	a = int(input('enter num >'))
	if a > max:
		max=a

print("num is " + str(max))
