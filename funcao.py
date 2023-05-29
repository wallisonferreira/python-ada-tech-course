
def saudacao():
    print('Seja bem-vindo')
    print('Olá')

saudacao()

# Função com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem-vindo, {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}')

saudacao('Wallison', 'Python')

# Função com parâmetros default

def saudacao(nome, curso='C++'):
    print(f'Seja bem-vindo, {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}')

saudacao('Wallison')

# Função com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é', resultado)

def calculadora(num1, num2, operacao='-'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(10, 20)

print(resultado)