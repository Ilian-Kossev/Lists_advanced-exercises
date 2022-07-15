collection_items_list = input().split(', ')
command = input()
while not command == 'Craft!':
    action = command.split(' - ')
    if action[0] == 'Collect':
        if action[1] in collection_items_list:
            pass
        else:
            collection_items_list.append(action[1])
    elif action[0] == 'Drop':
        if action[1] in collection_items_list:
            collection_items_list.remove(action[1])
    elif action[0] == 'Combine Items':
        new_action = action[1].split(':')
        if new_action[0] in collection_items_list:
            index = collection_items_list.index(new_action[0]) + 1
            collection_items_list.insert(index, new_action[1])
    elif action[0] == 'Renew':
        if action[1] in collection_items_list:
            collection_items_list.remove(action[1])
            collection_items_list.append(action[1])
    command = input()
print(', '.join(collection_items_list))
