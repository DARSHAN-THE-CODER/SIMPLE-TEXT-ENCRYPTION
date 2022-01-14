s=input("ENTER THE STRING TO BE ENCRYPTED:")

def encrypt(s):
    
    global a
    a=""
    for i in s:
        j=1
        a+=chr(ord(i)+5+j)
        j+=1
    return a[::-1]


k=encrypt(s)
print("ENCRYPTED TEXT IS :",k)

k=input("PRESS Y TO DISPLAY DECRIPTED TEXT:")

if k=="Y":
    def decrypt():
        b=""
        for i in a:
                k=1
                b+=chr(ord(i)-5-k)
                k+=1
        print("DECRYPTED TEXT IS :",b)
    decrypt()




