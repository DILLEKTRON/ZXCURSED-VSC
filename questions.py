# first
input_string = input()

words = input_string.split()

result_string = f"{words[1]} {words[0]}"

print(result_string)

# seconds
input_string = input()

first_index = input_string.find('f')
last_index = input_string.rfind('f')

if first_index == last_index and first_index != -1:
    print(first_index)
elif first_index != -1:
    print(first_index, last_index)

# third (F)
input_string = input()

first_index = input_string.find('f')
last_index = input_string.rfind('f')

if first_index == -1:
    print(-2)
elif first_index == last_index:
    print(-1)
else:
    print(last_index)
    
# four(G)
input_string = input()

first_index = input_string.find('h')
last_index = input_string.rfind('h')

if first_index != -1 and last_index != -1 and first_index != last_index:
    result_string = input_string[:first_index] + input_string[last_index + 1:]
    print(result_string)
else:
    print(input_string)

# fifth(X)
input_string = input()

first_index = input_string.find('h')
last_index = input_string.rfind('h')

if first_index != -1 and last_index != -1 and first_index != last_index:
    part_between_h = input_string[first_index + 1:last_index]

    result_string = input_string[:first_index + 1] + part_between_h + input_string[first_index + 1:]
    print(result_string)
else:
    print(input_string)
