#como fazer um gerenciador de tarefas em POO
#primeiro, vamos pensar, quais classes vamos precisar e o que cada classe precisa para ser criada:
#classes Tarefa   , Gerenciador.

class Tarefa:
    def __init__(self, categoria: str, descricao: str, urgencia: str, diasRestantes: int):
        self.categoria = categoria
        self.descricao = descricao
        self.urgencia = urgencia
        self.diasRestantes = diasRestantes
        self.status = "Pendente"

    def __str__(self):
        return f'{self.descricao} - {self.categoria} - {self.status}'

class Gerenciador:
    def __init__(self):
        self.listaTarefas = [
            Tarefa('casa', 'arrumar o quarto', 'leve', 2),
            Tarefa('casa', 'jogar o lixo', 'meio urgente', 1),
            Tarefa('estudo', 'estudar POO', 'leve', 1)
        ]

    def criarTarefa(self):
        print(f'{'-'*10}Criando Tarefa{'-'*10}')
        categoria = input('Categoria: ')
        descricao = input('Descricao: ')
        try:
            diasRestantes = int(input('Dias Restantes:'))
            urgencia = input('Urgencia: ')

            novaTarefa = Tarefa(categoria=categoria, descricao=descricao, urgencia=urgencia, diasRestantes=diasRestantes)
            self.listaTarefas.append(novaTarefa)
            print(f'Tarefa criada com sucesso!')
        except ValueError:
            print("Error do tipo de dados de cadastro")

    def listarTarefa(self):
        if not self.listaTarefas:
            print("Lista vazia")
        else:
            for i, tarefa in enumerate(self.listaTarefas, 1):
                print(f'Tarefa {i}: {tarefa}')

    def atualizarTarefa(self):
        self.listarTarefa()
        if self.listaTarefas:
            try:
                indice = int(input('Indice da tarefa: '))
                indice -= 1
                novostatus = input('Novo status: ')
                if 0 <= indice < len(self.listaTarefas):
                    self.listaTarefas[indice].status = novostatus
                else:
                    print("Indice invalido")
            except ValueError:
                print("Digite um valor inteiro")

    def deletarTarefa(self):
        self.listarTarefa()
        if self.listaTarefas:
            try:
                indice = int(input('Indice da tarefa: '))
                indice -= 1
                if 0<= indice < len(self.listaTarefas):
                    removido = self.listaTarefas.pop(indice)
                    print(f'Tarefa removida: {removido.descricao}')
                else:
                    print("Indice invalido")
            except ValueError:
                print("Digite um valor inteiro")

sistema = Gerenciador()
while True:
    print(f'\n{'-'*20}\nSISTEMA GERENCIADOR DE TAREFAS\n{'-'*20}\n')
    print('1 - Criar Tarefa\n2 - Listar Tarefas\n3 - Atualizar Tarefa\n4 - Deletar Tarefa\n5 - Sair')
    opcao = input('\nEscolha uma opcao: ')
    match opcao:
        case '1':
            sistema.criarTarefa()
        case '2':
            sistema.listarTarefa()
        case '3':
            sistema.atualizarTarefa()
        case '4':
            sistema.deletarTarefa()
        case '5':
            print('Saindo do Sistema...')
            break
        case _:
            print('Opcao invalida')