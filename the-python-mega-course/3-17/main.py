myList = ["python", "syntax", "reminds", "me", "of", "bash"]
print(myList)
print(len(myList))
print(myList[2])
print(myList[-1])

del myList[4]
print(myList)

myList = myList * 2
print(myList)

myList.append("syntax")
myList.insert(0, "intense")
print(myList)

myList.remove("python")
print(myList)
myList.remove("python")
print(myList)

# tuples are like lists but immutable
myTuple = ("python", "syntax", "reminds", "me", "of", "bash")
print(myTuple)
print(len(myTuple))
print(myTuple[2])
print(myTuple[-1])

myTuple = myTuple * 2
print(myTuple)
