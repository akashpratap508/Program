array1=[1,2,3,4,5,6,7]
max1=0
left=0
right=0
sum=int(input("enter the sum"))
for right in range(len(array1)):
    max1=max1+array1[right]
    while(max1>sum):
        max1=max1-array1[left]
        left +=1
    if sum==max1:
         print("Consecutive sum found between indices", left, "and", right)
    else:
         print("No consecutive sum found")
