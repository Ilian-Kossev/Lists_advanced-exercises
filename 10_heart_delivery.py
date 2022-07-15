neighbourhood_list = input().split('@')
command = input()
neighbourhood_list = [int(el) for el in neighbourhood_list]
step = 0
while not command == 'Love!':
    action = command.split()
    if action[0] == 'Jump':
        step += int(action[1])
        if step >= len(neighbourhood_list):
            step = 0
        if neighbourhood_list[step] == 0:
            print(f"Place {neighbourhood_list[step]} already had Valentine's day.")
        else:
            neighbourhood_list[step] -= 2
            if neighbourhood_list[step] == 0:
                print(f"Place {step} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {step}.")
if neighbourhood_list.count(0) == len(neighbourhood_list):
    print(f"Mission was successful.")
else:
    failed_places = len(neighbourhood_list) - neighbourhood_list.count(0)
    print(f"Cupid has failed {failed_places} places.")
# judge - 70/100



