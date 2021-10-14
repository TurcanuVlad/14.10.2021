a='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
b=''
print(a.replace(' ', '-', len(a)))
for i in range(0,len(a)):
    if(a[i]!="Z" and a[i]!=" "):
        b+=(chr(ord(a[i])+1))
    else:
        b+=a[i]
print("literele:")
print(b)
print("z cu a:")
print(a.replace("Z","A"))