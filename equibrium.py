array1=[1,2,6,4,0,-1]
array2=[]
max1=0
for i in range(len(array1)):
    max1=max1+array1[i]
    array2.append(max1)
print(array2)
length=len(array2)-1
if len(array1)<3 and len(array1)>1:
    print("there is no equilibriem in element in the array")
if len(array1)==1:
    print("the equilibrium elementis", array1[i])
else:
    for i in range(length-2, 1, -1):
        if array2[length]-array2[i]==array2[i-1]:
            print(i)
    print("the equilibrium elementis", array1[i])
