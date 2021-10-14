n=str(input("Introduceti sirul de caractere = "))
a=n.isupper()
ns=''
ns2=''
a='A'
lin='-'
n4=n
from string import ascii_letters
if a:
for c in n4:
if c in ascii_letters:
ns=ns+ascii_letters[(ascii_letters.index(c)+1)%len(ascii_letters)]
else:
ns+=c
ns=ns.replace("a","Z")
print('a) Sirul de caractere inlocuit = ',ns)
ns2=n.replace("Z","A")
ns2=ns2.replace(" ","-")
print('b,c) Stringul in care Z este inlocuit cu A si spatiul cu - = ',ns2)
else:
print('Eroare - sir de caractere inadmisibil')
