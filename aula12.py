nome = str(input('Qual é o seu nome? ')).capitalize()
if nome == 'José':
    print(f'Que nome lindo!')
elif nome == 'Maria' or nome == 'João' or nome == 'Pedro' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Joana Jéssica Bianca':
    print('Belo nome feminino')
else:
    print('Que nome horrível!')
print(f'Tenha um bom dia, {nome}!')


