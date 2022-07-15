n = int(input())
shell_list = []
shell_layer = 1
while n > 0:
    shell_electrons = 2 * shell_layer**2
    if shell_electrons <= n:
        shell_list.append(shell_electrons)
    else:
        remaining_shell_electrons = n
        shell_list.append(remaining_shell_electrons)
    shell_layer += 1
    n -= shell_electrons
print(shell_list)
