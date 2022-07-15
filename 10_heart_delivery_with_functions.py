def already_had_v_day(collection: list, index: int):
    if collection[index] == 0:
        print(f"Place {index} already had Valentine's day.")
        return True
    return False


def jump(collection: list, index: int, value: int):
    if not already_had_v_day(collection, index):
        collection[index] -= value
        if collection[index] == 0:
            print(f"Place {index} has Valentine's day.")
        else:
            return value


def success_count(collection: list):
    result = collection.count(0)
    if result == len(collection):
        print('Mission was successful.')
    else:
        failed_places = len(collection) - result
        print(f'Cupid has failed {failed_places} places.')


initial_list = input().split('@')
neighbourhood_list = [int(el) for el in initial_list]
command = input()
jump_length = 0
while not command == 'Love!':
    command_list = command.split()
    jump_length += int(command_list[1])
    if jump_length >= len(neighbourhood_list):
        jump_length = 0
    jump(neighbourhood_list, jump_length, 2)
    command = input()
print(f"Cupid's last position was {jump_length}.")
success_count(neighbourhood_list)

