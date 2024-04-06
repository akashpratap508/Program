list1=[5, 3, 4, 6, 7, 9, 8]
list2=[]
sum=0
for i in range(len(list1)):
    sum=sum+list1[i]
    list2.append(sum)
print(list2)
index1=int(input("enter the 1st index of an array : "))
index2=int(input("enter the 2nd index of an array : "))
def sum(index1, index2, list2):
    add=list2[index2]-list2[index1-1]
    print("Sum is : ",add)
sum(index1, index2, list2)
