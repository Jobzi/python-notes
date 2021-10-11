#Duplicates Not Allowed

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#Access set items
print("banana" in set1)

#set assign like constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)

#add set value
thisset.add("orange")
print(thisset)

#update set The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#remove set items
thisset.remove("banana")
print(thisset)

#pop 
x = thisset.pop()
print(x)
print(thisset)

#clear 
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

