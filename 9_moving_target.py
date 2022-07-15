target_sequence = input().split()
command = input()
target_sequence = [int(el) for el in target_sequence]
while not command == 'End':
    action = command.split()
    action[1] = int(action[1])
    action[2] = int(action[2])
    if action[0] == 'Shoot':
        if action[1] < len(target_sequence):
            target_sequence[action[1]] -= action[2]
            if target_sequence[action[1]] <= 0:
                target_sequence.pop(action[1])
    elif action[0] == 'Add':
        if int(action[1]) < len(target_sequence):
            target_sequence.insert(action[1], action[2])
        else:
            print('Invalid placement!')
    elif action[0] == "Strike":
        min_range = action[1] - action[2]
        max_range = action[1] + action[2]
        if min_range and max_range in range(len(target_sequence)):
            index = min_range
            i = min_range
            while i <= max_range:
                target_sequence.pop(index)
                i += 1
        else:
            print('Strike missed!')
    command = input()
target_sequence = [str(el) for el in target_sequence]
print('|'.join(target_sequence))
# Judge - 70/100



