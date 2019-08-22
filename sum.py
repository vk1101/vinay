x=[2,10,15,8]
b=0
for a in x:
    if b>a:
        print(a, 'is smaller than',b)
        b=b
    else:
        
        print(a, 'is greater than',b)
        b=a
print(b)