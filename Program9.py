n = input('Enter the number:')
s = input('Enter number to search:')
print("Number of occurance of ",s," in ",n," is ",n.count(s))

n = k = int(n)
s = int(s)
count = 0
while(n>0):
    x = n%10
    n = n//10
    if(x==s):
        count = count + 1
print("Number of occurance of ",s," in ",k," is ",count)