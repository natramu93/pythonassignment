#Create a program to display odd and even results from 0 to 30. (using ,for loop,while)

e = []
o = []
for a in range(0,31):
    if a%2==0:
        print(a,' is even')
        e.append(a)
    else:
        print(a,' is odd')
        o.append(a)

print('even',e)
print('odd',o)