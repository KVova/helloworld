KEY = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

import sys;

code_text = sys.argv[0:].replace(' ',''); 
Letter = ''
code_text = code_text.replace(' ','')
line_ab = ""
for letter in code_text:
    if letter.islower():
        line_ab += 'a'
    else: 
        line_ab += 'b'
 
d = len(line_ab)
for i in range(0,d,5):
    part = line_ab[i:i+5]
    if len(part) == 5:
       Letter += alphabet[KEY.find(part)]
 
print(Letter)