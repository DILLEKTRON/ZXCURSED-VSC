# first
numbers = list(map(int, input().split()))

print(len(set(numbers)))
# second
list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))

print(len(list1 & list2))
