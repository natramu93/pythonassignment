w = int(input('width:'))
h = int(input('height:'))
l = []
r = ''
for j in range (h):
    if (j==0 or j==(h-1)):
        for i in range(w):
            r = r+'*'
        l.append(r)
        r = ''
    else:
        for i in range (w):
            if(i==0 or i==(w-1)):
                r=r+'*'
            else:
                r = r+' '
        l.append(r)
        r = ''
for x in l:
    print(x)