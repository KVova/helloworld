import sys
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
a=str(sys.argv[1:])
a=a.replace(' ','')
 
#-----
ne=''
for i in a:
    if i.islower():
        ne=ne+'a'
    elif i.isupper():
        ne=ne+'b'
#-----    
p=''
d=[]
n=0
m=5
for i in alphabet:
    p=key[n:m]
    d.append(p)
    n=n+1
    m=m+1
#-----
z=0
c=5
q=()
let=''
letter=''
wen=''
i=1
 
while i<len(a):
    wen=ne[z:c]
    if len(wen)==5:
        q=d.index(wen)
        let=alphabet[q]
        letter=letter+let
    i=i+1
    z=z+5
    c=c+5
print(letter)