# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando listas
lista = []
lista = list()
lista = [26, 'Wallison', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])  # itera do index 2 ao 6 exclusive, dando 2 passos

# 1. utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. utilizando os índices

print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
    print(lista[i])

for _ in [10]:
    print("Olá, mundo")