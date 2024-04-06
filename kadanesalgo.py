list1=[-5, 1, -2, 3, -1, 2, -2]
length=len(list1)
print(length)
cs=0
ms=0
for i in range(length):
    cs=cs+list1[i]
    if cs<=0:
        cs=0
    
    if cs>0 and cs>ms:
        
        ms=cs
print(ms)
