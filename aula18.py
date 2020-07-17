import random
while True:
    jogadas = random.randint(1, 10)
    while True:
        perg = int(input('Digite o número que eu pensei: '))
        if perg == jogadas:
            print('Você ganhou!')
            break
        if perg > jogadas:
            print('O número é menor')
        if perg < jogadas:
            print('O número é maior')
    s_ou_n = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if s_ou_n == 'N':
        print('Obrigado por jogar!')
        break