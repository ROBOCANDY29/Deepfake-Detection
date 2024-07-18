def ctof():
    c=float(input("Enter temp in celsius:"))
    f=c*9/5+32
    print(f)
def si():
    p=int(input("Enter principal amount:"))
    r=int(input("Rate of interest:"))
    t=int(input("Enter Time:"))
    si=(p*r*t)/100
    amount=p+si
    print(amount)
def q3():
    i=int(input("First no:"))
    j=int(input("Second no:"))
    sum=i+j
    diff=i-j
    mul=i*j
    div=i/j
    print(f'Sum is {sum}\nDiff is {diff}\nMul is {mul}\nDiv is {div}')
def q4():
    a=int(input("a:"))
    b=int(input("b:"))
    print(f'a is {a}\nb is {b}')
    c=a
    a=b
    b=c
    print(f'a is {a}\nb is {b}')
def q5():
    a = int(input("a:"))
    b = int(input("b:"))
    print(f'a is {a}\nb is {b}')
    a,b=b,a
    print(f'a is {a}\nb is {b}')
q5()