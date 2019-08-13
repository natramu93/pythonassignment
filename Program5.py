l = int(input('Enter limit:'))
sum = 0
for k in range(1,l-1,2):
    sum += k
    print(k,end=' + ')
if(l%2 == 0):
    print(l-1,' = ',sum+l-1)
else:
    print(l,' = ',sum+l)

sum = 1
print(1,end='')
for k in range(3,l+1,2):
    sum += k
    print(' + ',k, end='')
print(' = ',sum)