import sys;
string = str(sys.argv[1]);
string_rep = string.replace(" ", "");
st_lower = string_rep.lower();
string_reversed = ' '.join(reversed(st_lower));
if string_reversed[::-1] == string_reversed:
    print("YES")
else:
    print("NO")