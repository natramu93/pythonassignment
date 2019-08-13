# Write a program which takes two integers N and M and produces last samples of N of the integers from N-1 to N-M.

n = int(input('Value of N:'))
m = int(input('Value of M:'))

for k in range(n-1,n-m-1,-1):
    print(k,end=' ')