import sys;

n1 = int(sys.argv[1]);
n2 = int(sys.argv[2]);

s = 0;

while n1 <= n2:
	arr = [int(x) for x in str(n1)]
	dov = len(arr)
	for count in range(6-(len(arr))):
		arr.insert(0, 0)
	if arr[0]+arr[1]+arr[2] == arr[3]+arr[4]+arr[5]:
		s +=1
	n1 +=1
print(s);