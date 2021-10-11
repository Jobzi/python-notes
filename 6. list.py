thislist = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
#List of Method

#append add otrer attrib to list
thislist.append("Orange")
thislist.append(b)
print(thislist)

#clear remove all elements the list
thislist.clear()
print(thislist)

#Copy one list to another list
c=b.copy()
print(c,b)

#count elements repeated of list
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9) #Output: 2

#extend a list to large list
b.extend(points)
print(b)

#index find the index the one element 
index=b.index(2)
print(index)

#list.insert(pos, elmnt) insert element in the position
b.insert(5,45)
print(b)

#pop() removes the element at the specified position
b.pop(5)
print(b)

#remove the element
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#reverse the order of the list
fruits.reverse()
print(fruits)

#sort the list alphabetically
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
