# Write a program which accepts 3 integers and sort them in ascending order.
ip = input('Enter 3 numbers (space separated):')
num = ip.split(' ')
l = []
for n in num:
    l.append(int(n))

if(l[0]>l[1]):
    t = l[0]
    l[0] = l[1]
    l[1] = t
if(l[0]>l[2]):
    t = l[0]
    l[0] = l[2]
    l[2] = t
if(l[1]>l[2]):
    t = l[1]
    l[1] = l[2]
    l[2] = t

print(l)