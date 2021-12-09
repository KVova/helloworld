import sys;
import math;

x = float(sys.argv[1]);
m = float(sys.argv[2]);
q = float(sys.argv[3]);

f = (1/(q*math.sqrt(2*math.pi)))* math.exp(-((math.pow((x-m),2)/(2*(math.pow(q,2))))));

print(f);