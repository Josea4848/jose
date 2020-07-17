import random
perguntas = ['Qual seleção foi campeã da copa do mundo de 2002?','8²?','2 + 5 x 4?','Qual o maior país em extensão territorial do mundo?']
resposta = ['BRASIL','64','22','RUSSIA']
score = 0
while True:
        if len(perguntas) > 0:
            if len(perguntas) > 1:
                sorteio = random.randint(0, (len(perguntas))-1)
            if len(perguntas) == 1:
                sorteio = 0
            print(perguntas[sorteio])
            resp = str(input('DIGITE A RESPOSTA:')).strip().upper()
            if resp == resposta[sorteio]:
                print('Acertou!')
                del perguntas[sorteio]
                del resposta[sorteio]
                score += 1
            else:
                print('Errou, Tente novamente!')
                print(f'Sua pontuação foi {score}')
                del perguntas
                break
        else:
            print('You winner!')
            break
