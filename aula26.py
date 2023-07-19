"""
    Formatação básica de strings

    s - string
    d - int
    f - float
    .<número de digitos>f (2.f para 2 casas decimais)
    x ou X - Hexadecimal
    (Caractere)(><^)(quantidade)
    > - Esquerda
    < - Direta
    ^ - Centro
    Sinal - + ou -
    Ex.: 0>-100,.1f
    Conversion flags - !r !s !a

""" 
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.4533131231:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')