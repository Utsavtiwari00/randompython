nSeries = int(input("enter the number: "))
n1=0
n2=1
if nSeries>=1:
    print(n1)
if nSeries>=2:
    print(n2)
for i in range(2,nSeries):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

