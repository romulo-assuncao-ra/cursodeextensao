#Fazendo um CRUD em POO
#Quais seriam as classes: Cliente, GerenciadorHotel


class Cliente:
    def __init__(self, nome: str, idade: int, documento: str, saldo: float, diasEstadia: int):
        self.nome = nome
        self.idade = idade
        self.documento = documento
        self.saldo = saldo
        self.diasEstadia = diasEstadia
        self.hospedado = False

    def custo_total(self, preco_diaria):
        return self.diasEstadia * preco_diaria

    def __str__(self):
        status = "Hospedado" if self.hospedado else "Não hospedado"
        return f'{self.documento} - {self.nome} - {status}'

class GerenciadorHotel:
    def __init__(self):
        self.listaClientes = [
            Cliente('Jonatas', 25, '12345678925', 1000, 3),
            Cliente('Genice', 28, '58964448925', 2000, 5),
            Cliente('Juan', 21, '58964448922', 2000, 5),
            Cliente('Jonnys', 18, '85236974221', 150, 5)
        ]

        self.precoDiaria = 130

    def buscarCliente(self, identificacao, mostrar: bool = False):
        identificacao = str(identificacao).strip().lower()
        resposta = [cliente for cliente in self.listaClientes if cliente.documento == identificacao]
        if resposta and mostrar: print((f'Cliente: {resposta[0]}'))
        return resposta[0] if resposta else None

    @staticmethod
    def validarCpfCliente(documento):
        return len(documento) == 11 and documento.isdigit()


    def criarCliente(self):
        print(f'Criando novo Cliente...')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        documento = input('CPF (Somente numeros): ')

        if self.buscarCliente(documento):
            print("Já existe um cliente com esse documento!")
            return

        if not self.validarCpfCliente(documento):
            print("CPF invalido")
            return

        dias = int(input('Quantos dias deseja estadiar: '))
        saldo = float(input('Quanto pretende gastar: '))
        novoCliente = Cliente(nome, idade, documento, saldo, dias)
        self.listaClientes.append(novoCliente)
        print('Cliente criado com sucesso!')

    def listarClientes(self):
        if not self.listaClientes:
            print("Lista vazia")
        else:
            for cliente in self.listaClientes:
                print(cliente)

    def removerCliente(self, identificacao):
        cliente = self.buscarCliente(identificacao)
        if cliente:
            self.listaClientes.remove(cliente)
            print(f'Cliente removido com sucesso: {cliente}')
        else:
            print('Cliente não encontrado!')

    def atualizarCliente(self, identificacao):
        cliente = self.buscarCliente(documento)
        if not cliente:
            print('Cliente não encontrado')
        else:
            if cliente.idade < 18:
                print("Menor de idade não pode fazer check-in sozinho")
                return
            custo = cliente.custo_total(self.precoDiaria)
            if custo > cliente.saldo:
                print("Saldo insuficiente para realizar check-in!")
                return
            cliente.hospedado = not cliente.hospedado #esse é o toggle

            acao = "CHECK-IN" if cliente.hospedado else "CHECK-OUT"
            print(f'{acao} realizado com sucesso')

hotel = GerenciadorHotel()
while True:
    print(f"\n{'='*20}\nSISTEMA GERENCIADOR DE HOTEL\n{'='*20}")
    try:
        escolha = int(input('1 - Criar | 2 - Buscar | 3 - Check-in/Check-out | 4 - Deletar | 5 - Sair: '))
        match escolha:
            case 1: hotel.criarCliente()
            case 2: hotel.buscarCliente(input('Digite o documento do cliente: '), mostrar = True)
            case 3: hotel.listarClientes()
            case 4: hotel.atualizarCliente(input('Digite o nome do cliente: '))
            case 5: hotel.removerCliente(input('Digite o cpf: '))
            case 6: break
            case _: 'Opção Inválida!'
    except ValueError:
        print('Erro, digite apenas números inteiros!')