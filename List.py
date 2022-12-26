l = ['krushna',45,78,'90',"aaruu"]
print(l)
print()
#list() function 
l = "krushna"
print(f"Given list is :: {l}")
x = list(l)
print(x)
print()
#split() function
l = "Python is dynamic language, It is very easy to learn"
print(f"Given list is :: {l}")
x = l.split()
print(x)
print()
#len() function
print(f"Given list is :: {l}")
print(f"Length of given list is {len(l)}")
print()
#count() function
l = [1,2,3,1,2,2,2,1,2]
print(f"Given list is :: {l}")
print(f"count of 1 in given list is : {l.count(1)}")
print(f"count of 2 in given list is : {l.count(2)}")
print(f"count of 3 in given list is : {l.count(3)}")
print(f"count of 4 in given list is : {l.count(4)}")
print()

#index() function
l = [1,2,2,1,2,2,3,1,2]
print(f"Given list is :: {l}")
print(f"first occurance of 1 in given list is at index {l.index(1)}")
print(f"first occurance of 2 in given list is at index {l.index(2)}")
print(f"first occurance of 3 in given list is at index {l.index(3)}")
print()

#append() function
l = [12,32,4,5,23,45]
print(f"Given list is : {l}")
print(f"Add element in the last of given list by using append function {l.append(34)}")
print(f"Updated list becomes :: {l}")
print()
#insert() function
print(f"Given list is : {l}")
print(f"Add element at any index of given list by using insert function {l.insert(2,67)}")
print(f"Updated list becomes :: {l}")
print()

l1 = [3,4,5,"k","f"]
l2 = [8,'r','p']
print(f'First list is :: {l1}')
print(f'Second list is :: {l2}')
l1.extend(l2)
print(f'List after extending ::{l1}')
print()

#remove() and pop()
l1.remove("k")
print(l1)
print(f"Pop element is :: {l1.pop()}")
print()

#reverse() and sort(),copy()
l1.reverse()
print(f"list in reverse form ::{l1}")
l.sort()
print(f"list in reverse form ::{l}")





