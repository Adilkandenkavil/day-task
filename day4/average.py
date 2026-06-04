def average(*args):
    avg=sum(args)/len(args)
    return avg
list1=[]
n=int(input("How many numbers do you want to enter?"))
for i in range(n):
    a=int(input(f"enter a mark{i+1}: "))
    list1.append(a)
x=average(*list1)
print("Average is",x)