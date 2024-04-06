array1=[1,2,3,4,5,6,7,8,9,10]
current_sum=0
maximum_sum=0
window=int(input("enter the size of the window"))
length=len(array1)
if length==0 or length<window:
    print(array1)
else:
    current_sum=sum(array1[:window])
    maximum_sum=current_sum
    for i in range(window, len(array1)):
        current_sum +=array1[i]-array1[i-window]
        maximum_sum=max(maximum_sum, current_sum)
    print(maximum_sum)
    print(i-window, "and", i)
