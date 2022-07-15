number_input = input().split(", ")
number_input_int = [int(el) for el in number_input]
boundary = 10
list_filtered_nums = []
while number_input_int:
    list_filtered_nums = [el for el in number_input_int if el <= boundary]
    num = 0
    while num < len(number_input_int):
        if number_input_int[num] <= boundary:
            number_input_int.remove(number_input_int[num])
            num -= 1
        num += 1

    print(f"Group of {boundary}'s: {list_filtered_nums}")
    boundary += 10