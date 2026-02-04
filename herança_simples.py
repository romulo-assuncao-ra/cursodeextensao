class Animal(object):
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print('Au au')

caramelo = Cachorro()
caramelo.falar()
