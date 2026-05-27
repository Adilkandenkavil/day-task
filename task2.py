#find second largest value without sorting
lis=[1,2,3,4,5,6]
lar=lis[0]
slar=lis[0]

for lis in lis:
    if lis>lar:
        slar=lar
        lar=lis
    elif lis>slar and lis != lar:
        lis=slar
print(slar)        



