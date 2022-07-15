input_list = input().split()
for el in input_list:
    el = list(el)
    value_concat_symbol = 0
    concat_symbol = ''
    while el:
        i = 0
        if ord(el[i]) in range(48, 58):
            concat_symbol += el[i]
            el.remove(el[i])
            i -= 1
        else:
            break
        i += 1
    value_concat_symbol = int(concat_symbol)
    first_letter = chr(value_concat_symbol)
    el.insert(0, first_letter)
    el[1], el[len(el) - 1] = el[len(el) - 1], el[1]
    print(''.join(el), end=' ')

