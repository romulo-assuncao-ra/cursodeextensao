def criarTarefa():
    categoria: str = input("Qual a categoria da tarefa? ")
    descricao: str = input("Descreva a tarefa: ")
    urgencia: int = int(input("Qual a urgência da tarefa? "))
    diasRestantes: int = int(input("Quantos dias restam para realizar a tarefa? "))

    return {
        "categoria": categoria,
        "descrição": descricao,
        "urgência": urgencia,
        "dias Restantes": diasRestantes,
    }


def concluirTarefa(tarefaId, listaTarefas):
    if tarefaId in listaTarefas.keys():
        listaTarefas.pop(tarefaId)
        print("Tarefa concluída com sucesso!")
        print("")
    else:
        print(
            "Essa tarefa não existe na lista, verifique o id das tarefas existentes\n"
        )
        print("")


def mostrarTarefas(listaTarefas: dict):
    if not listaTarefas:
        print("Não há tarefas na lista, que tal adicionar alguma?\n")
        print("")
    else:
        listaDescritiva = []
        for id, tarefa in listaTarefas.items():
            listaDescritiva.append(f"Id: {id}\nTarefa da categoria: {tarefa.get('categoria')}\nCom descrição: {tarefa.get('descrição')}\nUrgência: {tarefa.get('urgência')}\nTempo para concluir: {tarefa.get('dias Restantes')}")

        # listaDescritiva = [
        #     (f"Id: {id}\nTarefa da categoria: {tarefa.get('categoria')}\nCom descrição: {tarefa.get('descrição')}\n"
        #      f"Urgência: {tarefa.get('urgência')}\nTempo para concluir: {tarefa.get('dias Restantes')}")
        #     for id, tarefa in listaTarefas.items()
        # ] # List comprehension


        for tarefa in listaDescritiva:
            print(tarefa)
            print("")
        print("")


tarefas = {}
id = "0"

print("Bem vindo à sua lista de tarefas!")
while True:
    print(
        "O que deseja fazer?\n1: Criar nova tarefa\n2: Concluir alguma tarefa\n3: Mostrar todas as tarefas na lista\n4: Sair da lista de tarefas\n"
    )
    operacao = input()
    print("")
    match operacao:
        case "1":
            tarefa = criarTarefa()
            tarefas[id] = tarefa
            novoId = int(id) + 1
            id = f"{novoId}"
            print("Tarefa criada com sucesso!")
            print("")
        case "2":
            id = input(
                "Qual o Id da sua tarefa? Se não souber, veja todas as tarefas disponíveis com o comando 3."
            )
            print("")
            concluirTarefa(id, tarefas)
        case "3":
            mostrarTarefas(tarefas)
        case "4":
            break
        case _:
            print("Operação inválida! Digite uma das operações citadas")
            continue
