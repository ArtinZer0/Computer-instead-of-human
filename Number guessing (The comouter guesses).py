import  random
a=1
b=99
n=int(input("what uour number?"))
hads_C=0
while hads_C!=n:
    print("what youe gaus?")
    hads_C=random.randint(a,b)
    print(hads_C)
    if hads_C>n:
        print("loower")
        b=hads_C
    elif hads_C<n:
        print("upper")
        a=hads_C
print("nise cumputer !!!")
