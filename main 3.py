# lista mista
listaMista = [1, "oi", 3.14, True]
listaDeListas = [listaMista, [1, 2, 3]]

# Lista é mutável

listaVazia = list() # a mesma coisa de outraListaVazia
outraListaVazia = []
listaNumeros = list([1, 2, 3]) # ou list(range(4))
listCaracteres = list('Python')
#Resultado = ['P', 'y', 't', 'h', 'o', 'n']
listCaracteres[2] #acessando a letra 'T'
listCaracteres[-1] #acessa o ultimo

# Métodos de lista
listaNumeros.append(4) #acrescenta (int 4) no final
listaNumeros.remove(0) #remove o item pelo valor (1º que achar)
pop1 = listaNumeros.pop(1)
pop2 = listaNumeros.pop() #por padrão, deleta o último do item

listaCaracteres.index(1) #retorna o numero do index
len(listCaracteres) #retorna o numero total de elementos da lista

print('-' * 30)

#TUPLAS
#tuplas são imutáveis.
tuplaNumeros = tuple(listaNumeros)
outraTuplaNumeros = (5, 6, 7, 8, 9)
tuplaMista = (1, "oi", 3.14, True)

#Métodos de tupla
tuplaNUmeros.count(1) # conta quantos (1) tem na tupla
tuplaMista.index("oi")

print('-' * 30)

# DICIONARIOS
# pares de 'chave':'valor'
dictPessoa = {"nome": "Rômulo", "idade": 23} # tem 2 elementos
dictPessoa["nome"] #acessa o valor através da chave
dictPessoa["cidade"] = "Manaus"
dictPessoa.get("idade") #mais seguro, não quebra se não houver

# Métodos de dict
dictPessoa.get("idade", 0) ##caso não ache, o valor padrão será 0
dictPessoa.keys() #retorna todas as chaves
#resposta = ["nome", "idade", "cidade"]
dictPessoa.values() #retorna os valores
#resposta = ["Gustavo", 25, "Manaus"]
dictPessoa.items() #retorna pares (chave, valor)
#resposta = [("nome", "Gustavo"), ("idade",25), ("cidade", "Manaus")]
