import sys;

x = int(sys.argv[1]);
y = int(sys.argv[2]);
z = int(sys.argv[3]);

print ("Everybody sing a song:" + (' ' + 'la-' * (x-1) + 'la') * y + '!' * z + '.' * (1-z));