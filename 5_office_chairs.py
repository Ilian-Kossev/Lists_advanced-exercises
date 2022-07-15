room_num = int(input())
enough_chairs = True
total_chairs_num = 0
total_visitors_num = 0
n = 1
while n < room_num + 1:
    command = input().split()
    chair_num = len(command[0])
    total_chairs_num += chair_num
    visitors = int(command[1])
    total_visitors_num += visitors
    if chair_num < visitors:
        enough_chairs = False
        missing_chairs = visitors - chair_num
        print(f'{missing_chairs} more chairs needed in room {n}')
    n += 1
if enough_chairs:
    total_free_chairs = total_chairs_num - total_visitors_num
    print(f'Game On, {total_free_chairs} free chairs left')