# funções com argumentos nomeados vs. argumentos posicionais

# Função com argumentos posicionais
# TODA a função em python começa com um 'def'

#def somarPosicional(num1, num2):
#   print(f'O numero 1 tem valor: {num1}')
#  print(f'O numero 2 tem valor: {num2}')
#   return num1 + num2

#print(somarPosicional(4,8))

# Função com argumentos nomeados
def exponencialNomeado(num1=1, num2=1):
    print(f'O numero 1 tem valor: {num1}')
    print(f'O numero 2 tem valor: {num2}')
    return num1 ** num2

#print(exponencialNomeado(num2=2, num1=4))
#print(exponencialNomeado(num1=5))

#print() com argumentos extras
num1 = 10
num2 = 20
print(num1, num2, sep= ' - ', end='\n')

# F string
print(f'num é {num1} | {num2}')
print('num1 é {} | num2 é {}'.format(num1, num2))
print('num1 é {n1} | num2 é'.format(n1=num1, n2=num2))

# Operações Aritimética

print(f'Adição: {num1 + num2}')
print(f'Subtração: {num1 - num2}')
print(f'Multiplicação: {num1 * num2}')
print(f'Divisão: {num2 / num1}')
# resultado = 2.0 (float)
print(f'Divisão: {num2 // num1}') # divisão inteira
# resultado = 2 (inteiro)
print(f'Módulo: {num2 % num1}') # resto da divisão
print(f'exponencial: {num2**num1}')

# Operações Relacionais

print(f'Maior que: {num1 > num2}') # resposta = False
print(f'Maior igual a: {num1 >= num2}') #resposta = False
print(f'Menor que: {num1 < num2}') #resposta = True
print(f'Menor igual a: {num1 <= num2}') # resposta = True
print(f'É igual a: {num1 == num2}') # resposta = False
print(f'É diferente a: {num1 != num2}') # resposta = True

# Operadores Lógicos

num3 = 15
print(f'usando and: {num1 < num2 and num2 > num3}') # resposta = True
print(f'usando or: {num1 > num2 or num2 > num3}') # resposta = True
print(f'usando not: {not num1 > num2}') # resposta = True

cachorro1 = ['caramelo', 'pug', 'pretinho']
cachorro2 = cachorro1
cachorro3 = ['caramelo', 'pug', 'pretinho']

print(cachorro1 is cachorro2)
print(cachorro1 is cachorro3)

