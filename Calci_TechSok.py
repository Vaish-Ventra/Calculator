# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 09:01:23 2024

@author: ssvai
"""

# Calculator

# x^n


def Power(x, n):
    product = 1
    for i in range(1, (n+1)):
        product = product*x
    return product


def Fact(n):
    p = 1
    if n==0:
        return 1
    for i in range(1, n+1):
        p = p*i
    return p


def Sin(x):
    sum = 0.0
    for i in range(0, 10):
        s = Power((-1), i)
        xt = Power(x, (2*i)+1)
        f = Fact(2*i+1)
        sum = sum + (s*xt/f)
        ##print('s',xt, i, sum)
    return sum


def Cos(x):
    sum = 0.0
    for i in range(0, 10):
        s = Power((-1), i)
        xt = Power(x, (2*i))
        f = Fact(2*i)
        sum = sum + s*xt/f
        #print(i, s/f,"\n", sum)
    return sum


def Tan(x):
    return (Sin(x)/Cos(x))


def Sec(x):
    return 1/Cos(x)


def Cosec(x):
    return 1/Sin(x)


def Cot(x):
    return Cos(x)/Sin(x)


# nth root



def Find_upper(c, r, a, n):
    i = a
    if c == 0:
        #print("0 obviously")
        return 0
    while (Power(i, n)) <= c:
        i = i+r
        if (Power(i, n)) == c:
            #print(c, "^(1/", n, ") is ", i)
            return (-1)* i
        elif (Power(i, n)) > c:
            return i


def Find_lower(c, r, b, n):
    i = b
    while (Power(i, n)) >= c:
        i = i-r
        if (Power(i, n)) == c:
            #print(c, "^(1/", n, ") is ", i)
            return -1*i
        elif (Power(i, n)) < c:
            return i


def Nth_root(c, n):
    r = 16
    b = Find_upper(c, r, 0, n)
    while True:
        r = r/2
        a = Find_lower(c, r, b, n)
        if a<0:
            return -1*a
            break
        r = r/2
        b = Find_upper(c, r, a, n)
        if b<0:
            return -1*b
            break

        if r < 0.0001:
            #print(c, "^(1/", n, ") is ", (a+b)/2)
            return (a+b)/2
            break


def Pow2(x, n):
    #gn= int(n)
    # if n-gn==0:
    #    return Power(x,n)
    # else:
    # m = Power(x, (gn))
    # f=  n-gn
    # st= str(f)
    # n= len(st)
    # num= f* Power(10, n-2)
    # den=Power(10, n-2)

    # first alter nth root function so as to get the value returned not just printed
    return x**n

# log a base b


def ful(b, l, a, r):
    while Pow2(b, l) <= a:
        if Pow2(b, l) == a:
            print('wow', l)
            return -1
        l = l+r
        if Pow2(b, l) > a:
            return l


def fll(b, u, a, r):
    while Pow2(b, u) >= a:
        if Pow2(b, u) == a:
            print('wow', u)
            return -1
        u = u-r
        if Pow2(b, u) < a:
            return u


def Log(b, a):
    r = 16
    u = ful(b, 0, a, r)
    while True:
        r = r/2
        l = fll(b, u, a, r)
        if l == -1:
            break
        r = r/2
        u = ful(b, l, a, r)
        if u == -1:
            break
        if r < 0.01:
            print((l+u)/2)
            break


def Solve_Quad(a,b,c):
    D= (b*b) - (4*a*c)
    if D>0:
        d= Nth_root(D, 2)
        print ("Roots of the equaton are ", (-b+d)/(2*a), "and ", (-b-d)/(2*a))
    elif D==0:
        print ("The equation has only one root", -b/(2*a))
    else:
        d= Nth_root((-1*D), 2)
        print ("The equation has complex roots: (", -b, '+i', d, ')/', 2*a, "and (", -b, '-i', d, ')/', 2*a )

def Solve2lineareq(a1, b1, c1, a2, b2, c2):
    y= ((a1*c2)- (a2*c1))/((b1*a2)- (b2*a1))
    x=((b1*c2)- (b2*c1))/((a1*b2)- (a2*b1))
    return [x,y]
        
   

while True:
    x = int(input('''Type 1 for addition, subtraction, multiplication and division 
    u can use the normal operators.
    2 for log 
    3 To find nth root 
    4 for sin
    5 for cos 
    6 for tan
    7 for cosec
    8 for sec 
    9 for cot
    10 to find roots of a quadratic equation
    11 to find the solution of 2 linear equations(in 2 variables)
    Anything else to exit calculator
        :-'''))
    if x == 1:
        n1 = int(input('n1= '))
        o = input('operation= ')
        n2 = int(input('n2= '))
        if o == '+':
            print('\n=', n1+n2)
        elif o == '-':
            print('\n=', n1-n2)
        elif o == '*':
            print('\n=', n1*n2)
        elif o == '/':
            print('\n=', n1/n2)
        else:
            print('invalid operator')
    elif x == 2:
        bs = int(input('base= '))
        a = float(input('argument(that is a)= '))
        print('\n')
        Log(bs, a)
    elif x==3:
        c= float(input("number= "))
        n= int (input('enter n in nth root= '))
        print ('\n')
        Nth_root(c, n)
    elif x==4:
        n= float(input("Enter angle in radians: "))
        print ('sin(', n, ")=", Sin(n))
    elif x==5:
        n= float(input("Enter angle in radians: "))
        print ('cos(', n, ")=", Cos(n))
    elif x==6:
        n= float(input("Enter angle in radians: "))
        print ('tan(', n, ")=", Tan(n))
    elif x==7:
        n= int(input("Enter angle in radians: "))
        print ('cosec(', n, ")=", Cosec(n))
    elif x==8:
        n= float(input("Enter angle in radians: "))
        print ('sec(', n, ")=", Sec(n))
    elif x==9:
        n= float(input("Enter angle in radians: "))
        print ('cot(', n, ")=", Cot(n))
    elif x==10:
        a= float(input("Enter a: "))
        b= float(input("Enter b: "))
        c= float(input("Enter c: "))
        Solve_Quad(a, b, c)
    elif x==11:
        print ('''Let the equations be
               a1x + b1y + c1 = 0
               a1x + b1y + c1 = 0''')
        a1= float(input("Enter a1: "))
        b1= float(input("Enter b1: "))
        c1= float(input("Enter c1: "))
        a2= float(input("Enter a2: "))
        b2= float(input("Enter b2: "))
        c2= float(input("Enter c2: "))
        print( Solve2lineareq(a1, b1, c1, a2, b2, c2))
    else:
        print ('exited')
        break
        
