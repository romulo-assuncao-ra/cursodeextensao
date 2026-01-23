
umaVariavel = 10
print(f'{umaVariavel} é {type(umaVariavel)}')

umaVariavel = "Hello World"
print(f'{umaVariavel} é {type(umaVariavel)}')

umaVariavel = 10.5
print(f'{umaVariavel} é {type(umaVariavel)}')

umaVariavel = True
print(f'{umaVariavel} é {type(umaVariavel)}')

umaVariavel = None
print(f'{umaVariavel} é {type(umaVariavel)}')


#Type Hint ( dica de tipo )
variavelNumero: int = 10
variavelFloat: float = 3.14
variavelString = str = "Hello World"
variavelBoolean = True

#input
exemploInput1 = int (input("Digite um numero:"))
exemploInput2 = int (input("Digite outro numero:"))

print(f'A soma é: {exemploInput1 + exemploInput2}')