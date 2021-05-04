N=int(input())
def binary(n):
    l=[]
    a=n
    while a>1:
        l.append(a%2)
        a//=2
    l.append(a)
    l.reverse()
    s=str()
    for k in range(len(l)):
        s+=str(l[k])
    return s
#print(binary(N)): work
def bi(n):
    if n==1:
        return 1
    elif n>1:
        if n%2==1:
            s=str(bi(n//2))+'1'
        elif n%2==0:
            s=str(bi(n//2))+'0'
        return s
print(bi(N))