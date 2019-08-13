# Create a program to display sum of even results find the result and check whether it is odd or even? (Range is 0 to 50)
e = []
o = []
for a in range(0,51):
    if a%2==0:
        print(a,' is even')
        e.append(a)
    else:
        print(a,' is odd')
        o.append(a)

print('even',e)
print('odd',o)
esum = 0
osum = 0
for k in e:
    esum = esum + k
for k in o:
    osum += k
print('sum of even numbers ',esum)
print('sum of odd numbers ',osum)
if(esum%2==0):
    print('sum of even numbers is even')
else:
    print('sum of even numbers is odd')

if(osum%2==0):
    print('sum of odd numbers is even')
else:
    print('sum of odd numbers is odd')

