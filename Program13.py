x = int(input('Enter a number:'))
l = []
for num in range(1,x+1):
    sum = 0
    for n in range(1,num):
        if(num%n==0):
           sum += n
    if(sum>num):
        l.append(num)
print('list of abundant numbers is ',l)