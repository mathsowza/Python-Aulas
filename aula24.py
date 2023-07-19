# Operadores in e not in
# String são iteráveis
#  0 1 2 3 4 5 6
#  M A T H E U S
# -7-6-5-4-3-2-1

# nome = 'Matheus'
# print('theus' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('theus' not in nome)
# print('zero' not in nome)
# print(nome[-5])
# print(nome[-7])
# print(nome[-1])

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')