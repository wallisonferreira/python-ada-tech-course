
"""for variavel in range(5):
    print(variavel)"""

"""for variavel in range(5,11):
    print(variavel)"""

for variavel in range(1,12,3):
    print(variavel)

# Como podemos evitar esta repetição?

"""nota1 = float(input("Informe sua nota 1"))
nota2 = float(input("Informe sua nota 2"))
nota3 = float(input("Informe sua nota 3"))
"""

# Podemos criar uma estrutura controlada de repetição (for)

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))

    soma = soma + nota

print(soma / 3)
