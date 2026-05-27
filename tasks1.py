#remove dublicate
l=[1,2,2,3,4,4,5,6]
l.remove(2)
l.remove(4)
print(l)

#exact method
lis=[1,2,2,3,4,4,5,6]
result=[]

for i in lis:
    if i  not in result:
        result.append(i)
print(result)        

