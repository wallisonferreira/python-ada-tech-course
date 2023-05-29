dicionario = {}
dicionario = dict()

dicionario = {
    'nome': 'Wallison',
    'idade': 26,
    'altura': 1.77
}

#print(dicionario)
#print(dicionario['idade'])

dicionario['programador'] = True
dicionario[(1,2,3)] = True

dicionario['altura'] = 2

#print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)