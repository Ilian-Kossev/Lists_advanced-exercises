current_version = input().split('.')
new_version = [int(el) for el in current_version]
new_version[2] += 1
if new_version[2] == 10:
    new_version[2] = 0
    new_version[1] += 1
    if new_version[1] == 10:
        new_version[1] = 0
        new_version[0] += 1
str_new_version = [str(el) for el in new_version]

print('.'.join(str_new_version))