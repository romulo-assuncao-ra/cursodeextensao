#Vamos fazer um jogo RPG em POO
#Personagem (ambos, jogador e inimigo), JogoRPG (gerenciador dos personagens)
import random as rd

class Personagem:
    def __init__(self,nome: str, vida: int, defesa: int, ataque: int):
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo):
        dano = max(self.ataque - alvo.defesa, 0)
        alvo.vida -= dano
        return dano

    def fortalecer(self, valor=2):
        self.defesa += valor

    def curar(self, valor=10):
        self.vida = min(self.vida+valor, 100)

class JogoRPG:

    def __init__(self):
        nome_player = input('Qual o seu nome? ')
        self.player = Personagem(nome_player, 100, 10, 10)
        self.inimigo = Personagem ( "BOSS", 100, 9, 15)

    def iniciar_jogo(self):
        print(f'Batalha entre {self.player.nome} e {self.inimigo.nome}')
        while self.player.esta_vivo() and self.inimigo.esta_vivo():
            self.turno_jogador()
            self.turno_inimigo()
        self.finalizar_jogo

    def turno_jogador(self):
        print(f'{self.player.nome}: {self.player.vida} HP | {self.inimigo.nome}')
        escolha =  input('Ação: [1] atacar | [2] Fortalecer | [3] Curar: \n')
        if escolha == '1':
            dano = self.player.atacar(self.inimigo)
            print(f'{self.player.nome} atacou {self.inimigo.nome} e causou {dano} de dano!')
        elif escolha == '2':
            valor_dado = rd.randint(1, 6)
            self.player.fortalecer(valor_dado)
            print(f'{self.player.nome} aumentou seu ataque em {valor_dado}! ')
        elif escolha == '3':
            valor_cura = rd.randint(2, 7)
            self.player.curar(valor_cura)
            print(f'{self.player.nome} curou {valor_cura} de vida! ')
        else:
            'Escolha um valor válido'

    def turno_inimigo(self):
        acao = rd.choice(['atacar', 'fortalecer', 'curar'])
        match acao:
            case 'atacar':
                dano = self.inimigo.atacar(self.player)
                print(f'{self.inimigo.nome} atacou {self.player.nome} e causou {dano} de dano!')
            case 'fortalecer':
                valor_dado = rd.randint(2, 6)
                self.inimigo.fortalecer(valor_dado)
                print(f'{self.inimigo.nome} aumentou seu ataque em {valor_dado}! ')
            case 'curar':
                valor_cura = rd.randint(4, 10)
                self.inimigo.curar(valor_cura)
                print(f'{self.inimigo.nome} curou {valor_cura} de vida!')

    def finalizar_jogo(self):
        print(f'{self.player.nome}perdeu !') \
            if not self.player.esta_vivo() \
            else print(f'Parabéns {self.player.nome} ganhou!')

if __name__ == '__main__':
    jogo = JogoRPG()
    jogo.iniciar_jogo()





