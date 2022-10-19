#creatine a list
# var1 = ["monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# print(var1[1])

#length of a string
# var1 = list(("monday", "tuesday", "wednesday", "thursday"))
# print(f"length of var1: {len(var1)}")

#Indexing strings
# print(var1[-3])

#editing Lists
# var1[0] = "friday"
# print(var1)

#Inserting into List
# var1.insert(0, "monday")
# print(var1)

#Inserting into the end of the list
# var1.append("friday")
# print(var1)

#Adding a list to another list
# weekend = ["Saturday", "Sunday"]
# print(var1)
# print(weekend)
# var1.extend(weekend)
# print(var1)

#Removing Elements from the List using the element name
# var1.remove("monday")
# print(var1)

#Removing elements from a list using the index
# var1.pop(1)
# print(var1)

#Delete elements from a list you can also use is the index
# del var1
# print(var1)

#Removing elements from the list and retaining the braces &space
# var1.clear()
# print(var1)

# #sorting elements in a list
# age = [12, 1, 5, 15, 56, 167, 78, 89, 90]
# age.sort()
# print(f"sorted: {age}\n")
#
# age = [12, 23, 34, 45, 56, 67, 78, 89, 90]
# print(f"unsorted: {age}")


age = [12, 23, 34, 45, 56, 67, 78, 89, 90]
print(f"unsorted: {age}")
age.sort()
print(f"Ascending: {age}")
age.sort(reverse=True)
print(f"Anything: {age}")





