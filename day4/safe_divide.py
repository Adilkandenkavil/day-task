def safe_divide(a,b):
    if b==0:
        raise MyError("Denominator must not be zero")
    result=a/b
    return result
a=int(input("enter a number:"))
b=int(input("enter a number:"))
class MyError(Exception):
    pass

try:
    print(safe_divide(a,b))
except MyError as e:
    print("type non zero number ",e)