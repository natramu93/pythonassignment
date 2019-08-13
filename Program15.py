# Write a program which accepts an integer and print its factors but the factors must be prime.

ip = int(input('Enter a number:'))
l = []
pl = []
for n in range(2,ip):
    if(ip%n==0):
        l.append(n)
print('factors are',l)
pf = True
for n in l:
    for x in range(2, n):
        if (n % x == 0):
            pf = False
            break
    if(pf):
        pl.append(n)
print('prime factors are',pl)
n=2
while(ip>0):
    if(ip%n==0):
        print(n,end=' ')
        ip = ip//n
        n = 2
    else:
        n = n+1