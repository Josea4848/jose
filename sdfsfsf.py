import random
import time
print('\033[34m','=-'*5,'\033[35mJo\033[33mken\033[32mpô','\033[34m=-'*5)
jogadas = ['PEDRA', 'PAPEL', 'TESOURA','PAPEL','TESOURA','PEDRA']
s  = decisao = 0
spc = 0
while True:
        for c in range (1,4):
            print(f'\033[1;30mRodada {c}')
            time.sleep(0.8)
            jogador = str(input('\033[mEscolha entre PEDRA, PAPEL E TESOURA:')).upper().strip()
            s1 = random.choice(jogadas)
            print('\033[1;35mJO')
            time.sleep(1)
            print('\033[1;33mKEN')
            time.sleep(1)
            print('\033[1;32mPÔ')
            time.sleep(1)
            print(f'\033[1;31mPC- \033[m{s1}!!!')
            time.sleep(0.8)
            #jogador ganhou

            if 'PAPEL' in jogador and 'PEDRA' in s1 or 'TESOURA' in jogador and 'PAPEL' in s1 or 'PEDRA' in jogador and 'TESOURA' in s1:
                print('\033[32mUM PONTO PARA \033[1;32mVOCÊ!!!')
                s += 1
                spc += 0
                #empate
            elif jogador == s1:
                print('\033[34mNINGUÉM PONTOU!!')
                s += 0
                spc += 0
                #pc ganhou
            else:
                print('\033[31mPONTO PARA O \033[1;31mPC!')
                s += 0
                spc += 1
        print(f'\033[m==========\033[1;34mPLACAR\033[m===========')
        print(f'\033[32mVOCÊ: \033[m{s} ponto(s)\033[m')
        print(f'\033[31mPC: \033[m{spc} ponto(s)\033[m')
        print('=' * 27)
        if s > spc:
            print('\033[2;32mVocê Ganhou!!')
        elif s == spc:
            print('\033[2;34mEmpate!')
        else:
            print('\033[4;31mVOCÊ PERDEU!')
        decisao = str(input('\033[mJogue novamente [S/N]: ')).upper()
        if decisao == 'N':
            break
print('Encerrando...')
time.sleep(2)
