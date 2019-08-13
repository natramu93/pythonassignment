min = int(input('Number to Start:'))
max = int(input('Number to end:'))
pcount = 0
count = 0
for num in range(min,max+1):
    pcount = pcount + str(num).count('1')
    n = k = num
    while(n>0):
        x = n%10
        n = n//10
        if(x==1):
            count = count + 1
print("Number of occurance of ",1," in the range of ",min," to ",max," is ",count)
print(pcount)