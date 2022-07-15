list_string_1 = input().split(', ')
list_string_2 = input().split(', ')
new_string = []
for el in list_string_1:
    for string in list_string_2:
        if el in string and el not in new_string:
            new_string.append(el)
print(new_string)

