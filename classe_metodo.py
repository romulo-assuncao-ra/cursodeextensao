class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome: str = nome
        self.idade: int = idade

    def greet(self) -> None:
        print(f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.')

class Carro:
    def __init__(self, marca: str, modelo: str, color: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ano = ano

    def ligar_motor(self):
        print(f'Ligando motor de {self.marca}')

    def desligar_motor(self):
        print(f'Desligando motor de {self.marca}')

meuCarro = Carro('BYD', 'Dolphin', 'Preto', 2025)
meuCarro.ligar_motor()