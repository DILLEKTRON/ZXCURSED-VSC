# Задние 1
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

list3 = list1 + list2
print(list3)
# Задание 2
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

list3 = list(set(list1 + list2))
print(list3)
# Задание 3
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

list3 = list(set(list1) & set(list2))
print(list3)
# Задание 4
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

list3 = list(set(list1) ^ set(list2))
print(list3)
# Задние 5
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

list3 = [min(list1), max(list1), min(list2), max(list2)]
print(list3)
