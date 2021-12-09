# import sys;

# arr = (sys.argv[1:]);

# for i in arr[::-1]:
	# print(i, end=' ');
	
import sys;

n = (sys.argv[1:]); 
arr = ' '.join(n[::-1]);

print(arr)