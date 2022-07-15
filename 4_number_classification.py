number_list = [int(el) for el in input().split(", ")]
positive_nums = ', '.join([str(el) for el in number_list if el >= 0])
negative_nums = ', '.join([str(el) for el in number_list if el < 0])
odd_nums = ', '.join([str(el) for el in number_list if el % 2 == 1])
even_nums = ', '.join([str(el) for el in number_list if el % 2 == 0])
print(f'Positive: {positive_nums}')
print(f'Negative: {negative_nums}')
print(f'Even: {even_nums}')
print(f'Odd: {odd_nums}')
