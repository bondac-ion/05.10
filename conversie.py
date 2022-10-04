import random
m=random.randint(10,999)
n=random.randint(10,999)
b=random.randint(2,9)
m_1=[]
for i in str(m):
    m_1.append(int(i))
n_1=[]
for i in str(n):
    n_1.append(int(i))
if max(m_1)<b and max(n_1)<b:
    def baza(x):
        z=str(x)
        stri=[]
        global b
        if len(z)>1 and len(z)<=3:
            if b>=2 and b<=9:
                for i in z:
                    stri.append(int(i))
                if max(stri)<b:
                    return True
                else:
                    return False
    def baza_10(x):
        if baza(x)==True:
            baza_10_nr=0
            z=str(x)
            global b
            for i in range(int(len(z))-1,-1,-1):
                baza_10_nr+=int(z[i])*(b**abs(i-int(len(z))))
            return int(baza_10_nr/b)
    print("Numarul",m,"e scris corect",baza(m))
    print("Numarul",n,"e scris corect",baza(n))
    print("Baza este ",b)
    def schimb_de_baza(x):
        baza_1=[]
        baza_2=""
        global b
        while(x!=0):
            baza_1.append(x%b)
            x=x//b
        if max(baza_1)<b:
            baza_1.reverse()
            for i in baza_1:
                baza_2+=str(i)
            return int(baza_2)
    print("Suma de m+n in baza",b,"=",schimb_de_baza(baza_10(m)+baza_10(n)))
    if m>=n:
        print("Diferentei de m-n in baza",b,"=",schimb_de_baza(baza_10(m)-baza_10(n)))
        print("Diferenta de m-n in baza",b,"=",-1*(schimb_de_baza(baza_10(m)-baza_10(n))))
    else:
        print("Diferentei de m-n in baza",b,"=",schimb_de_baza(baza_10(n)-baza_10(m)))
        print("Diferenta de m-n in baza",b,"=",-1*(schimb_de_baza(baza_10(n)-baza_10(m))))
    print("Podusul m*n in baza",b,"=",schimb_de_baza(baza_10(m)*baza_10(n)))
else:
    print("mai incearca odata")