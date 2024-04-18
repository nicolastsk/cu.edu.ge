def bobs(a):
    b=0
    for i in range(len(a)-1):
        if a[i-1:i+2] == "bob":
            b+=1
    return b
print(bobs("baobadasdbobawdasbobaws"))

def subo(a):
    b=a[0]
    c=''
    for i in range(len(a)):
        if len(b)>len(c):
            c=b
        if a[i]>=a[i-1]:
            b+=a[i]
        else:
            b=a[i]
    return c
print(subo('abcdsgesgofedasdbvjih'))

def squarewhile(a):
    b=2
    c=1
    while b>0:
        c*=a
        b-=1
    return c
print(squarewhile(5))

def cuberootwhile(a):
    b=0
    while b**3<abs(a):
        b+=1
    if b**3 !=abs(a):
        return "you are not a root"
    if a<0:
        b=-b
    return b
print(cuberootwhile(-8))

def cubefor(a):
    for i in range (a+1):
        if i**3==a:
            return i
print(cubefor(-8))

def bindec(a):
    b=len(a)-1
    c=0
    for i in a:
        if i=='1':
            c+=2**b
        b-=1
    return c
print(bindec('101101'))

def decbin(a):
    result=''
    while a>0:
        result+=str(a%2)
        a=a//2
    return result
print(decbin(45))

def decbinrec(a):
    if a == 0:
        return '0'
    elif a == 1:
        return '1'
    else:
        return decbinrec(a // 2) + str(a % 2)
print(decbinrec(45))

def multit(a,b):
    result=0
    while b>0:
        result+=a
        b-=1
    return result
print(multit(5,4))

def factit(a):
    b=1
    while a>0:
        b*=a
        a-=1
    return b
print(factit(5))

def factrec(a):
    if a==1:
        return 1
    else:
        return a*factrec(a-1)
print(factrec(5))

def recpow(a,b):
    if b==1:
        return a
    else:
        return a*recpow(a,b-1)
print(recpow(5,3))
def itpow(a,b):
    c=1
    while b>0:
        c*=a
        b-=1
    return c
print(itpow(5,2))

def gcditer(a,b):
    c=min(a,b)
    while c>0:
        if a%c==0 and b%c==0:
            return c
        else:
            c-=1
print(gcditer(10,4))

def gcdrec(a,b):
    if b==0:
        return a
    else:
        return gcdrec(b,a%b)
print(gcdrec(25,5))

def palrec(a):
    if len(a)==1:
        return True
    else:
        return a[0]==a[-1] and palrec(a[1:-1])
print(palrec('opopopopo'))

def cube_root_bisectional(num, epsilon=0.00001):
    low = 1
    high = num
    guess = (low + high) / 2
    while abs(guess**3 - num) >= epsilon:
        if guess**3 < num:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess
number = 27
print("Cube root of", number, "is approximately:", cube_root_bisectional(number))

def cube_root_newton_raphson(num, epsilon=0.00001):
    if num == 0:
        return 0
    guess = num / 2
    while abs(guess**3 - num) >= epsilon:
        guess = guess - (guess**3 - num) / (3 * guess**2)
    return guess
number = 27
print("Cube root of", number, "is approximately:", cube_root_newton_raphson(number))

def fibrec(a):
    if a==0 or a==1:
        return 1
    else:
        return fibrec(a-1) + fibrec(a-2)
print(fibrec(5))

def fibit(a):
    b, c = 1, 1
    while a > 1:
        b, c, a = c, b + c, a - 1
    return c
print(fibit(5))

def oddtuples(a):
    b=()
    for i in range(len(a)):
        if i % 2 ==0:
            b+=(a[i],)
    return b
a=('i','am','a','test','tuple')
print(oddtuples(a))

import random as r
def lista(a):
    b,c=[],[]
    for i in range(len(a)):
        if a[i] % 2 == 1:
            b.append(a[i])
        if i%2==1:
            c.append(a[i])
    return sum(a),sum(b),sum(c)
a=[r.randint(0,100)for i in range (20)]
print(lista(a))

def applytoeach(L,f):
    for i in range(len(L)):
        L[i]=f(L[i])
    return L
print(applytoeach([5,6.2,-8,9.2],abs))

def applytoeach2(L,x):
    for f in L:
        print(f(x))
applytoeach2([int,abs],-5.2)

