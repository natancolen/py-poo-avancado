class Programa():
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def imprimir(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprimir(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprimir(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes'

if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 149)
    monstro_pantano = Serie('monstro do pantano', 2019, 1)

    vingadores.dar_like()
    monstro_pantano.dar_like()
    monstro_pantano.dar_like()

    filmes_e_serie = [vingadores, monstro_pantano]

    for programa in filmes_e_serie:
        print(programa.imprimir())

