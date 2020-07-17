a = int(input('\033[33mDigite um valor\033[m: '))
b = int(input('\033[36mDigite outro valor\033[m: '))
print(f'\033[30mA soma entre \033[4;33m{a}\033[30m e \033[4;36m{b}\033[m \033[30mé \033[1;31m{a + b}\033[m')
