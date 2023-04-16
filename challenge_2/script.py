r,n={'I':1,'V':5,'X':10,'L':50,'C':100,'M':1000},{1000:'M',100:'C'}
def c(i):
    d,p=0,0
    for n in i[::-1]:
        v=r[n]
        if v<p:d-=v
        else:d += v
        p=v
    return d
h,k=1100,''
for v in n.keys():k+=n[v]
print(k,'since',''.join(str(c(i))+'/'for i in "V/III/MCMLXXXV".split("/"))[:-1])


