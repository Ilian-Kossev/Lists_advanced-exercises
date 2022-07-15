input_string = input().split()
output_list = [el for el in input_string if len(el) % 2 == 0]
for el in output_list:
    print(el)


