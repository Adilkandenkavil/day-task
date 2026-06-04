a=input("enter a number: ")
words=a.split()
for word in set(words):
    print(word,":",words.count(word))
