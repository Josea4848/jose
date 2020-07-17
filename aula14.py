n = 1
cont = 0
cont2 = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            cont+=1
        else:
            cont2 += 1
print(f'Foram {cont} par(es) e {cont2} ímpar(es)')
