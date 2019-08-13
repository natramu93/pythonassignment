# Create a program to display multiplication table of 5 until the upper limit is 30
# And find the even and odd results and also find the count of even or odd results and display at the end. (using do while loop,for loop,while)
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 30 = 150
e= []
o= []
for a in range(1,31):
    if (a*5)%2==0:
        print(5,' X ',a,' = ',5*a,' is even')
        e.append(a*5)
    else:
        print(5,' X ',a,' = ',5*a,' is odd')
        o.append(a*5)

print('even results ',e)
print('odd results ',o)

print('count of even results ',len(e))
print('count of odd results ',len(o))