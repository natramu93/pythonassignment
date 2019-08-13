# Write a program which takes input as integer and display the binary triangle on the basis of input integer.
# Example: 1.If user gives input 5 then the binary triangle should be like this : 1 01 010 1010 10101

rows = int(input('Number of Rows:'))
x=1
for i in range(1,rows+1):
    for j  in range(1,i+1):
        print(x,end='')
        x += 1
        x = x%2
    print()
