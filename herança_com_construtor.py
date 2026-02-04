class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Estudante(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula

marcos = Estudante('Marco','1234')
print(marcos.nome, marcos.matricula)