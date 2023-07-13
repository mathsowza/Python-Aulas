import datetime

ano_atual = datetime.datetime.now()
data = ano_atual.date()
ano = data.strftime("%Y")
nome = 'Matheus'
sobrenome = 'Silva'
idade = 27
ano_nascimento = (int)(ano) - idade
maior_de_idade = idade >= 18
altura_metros = '1.80m'

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura:', altura_metros)
