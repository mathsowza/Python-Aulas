"""Interpolação Básica de Strings

    s - string
    d e i - int
    f - float
    x e X - hexadecimal
"""

nome = 'Matheus'
preco = 1000.09874098
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))