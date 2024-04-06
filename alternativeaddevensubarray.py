list=[10, 12, 14, 7 ,8]
cm=1
ml=1
for i in range(1, len(list)):
    if list[i]%2!=list[i-1]%2:
        cm=cm+1
    if cm>ml:
        ml=cm
print(ml)
