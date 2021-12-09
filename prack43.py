import sys;
	
n = sys.argv[1]

if n == "":
	print ('YES')

if n.find(')') == 0:
	print ('NO')

else:
	for i in range(len(n)):

		c = n.find('(')
		z = n.find(')')

		n = n[0:abs(c)] + n[(abs(c) + 1):]
		n = n[0:abs(z-1)] + n[abs(z):]

		if (z == -1) and (c == -1):
			print ('YES')
			break

		elif (z == -1 and c == 0) or (z == 0 and c == -1):
			print ('NO')
			break