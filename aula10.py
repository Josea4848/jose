nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1+nota2+nota3)/3
print('Carregando resultado...')
if media < 7:
    print(f'Sua média foi {media:.1f}, e você não foi aprovado! :(')
else:
    print(f'Parabéns! Sua média foi {media:.1f} e você foi aprovado')

