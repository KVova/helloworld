import sys;

f1 = 1;
f2 = 1;
i = 0

n = int(sys.argv[1]);

while i < n - 2:
	s = f1 + f2
	f1 = f2
	f2 = s
	i +=1
if n == 0:
	print (0);
else:
	print(f2);