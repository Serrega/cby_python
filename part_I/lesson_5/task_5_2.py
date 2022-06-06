list1 = [n for n in range(2, 51, 4)]
print(list1)
list2 = [100 - m*3 for m in range(12)]
print(list2)
list3 = [m for m in range(100, 66, -3)]
print(list3)
languages = 'Python Golang PHP C# Java'
dict1 = {x: x[0] for x in languages.split(' ')}
print(dict1)
