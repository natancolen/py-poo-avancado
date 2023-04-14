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

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes'
class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


if __name__ == '__main__':
    hercules_disney = Filme('Hecules', 1997, 93)
    homem_aranha_svpc = Filme('homem aranha - sem volta para casa', 2022, 148)
    homem_de_ferro = Filme('Homem de Ferro', 2008, 126)
    vingadores = Filme('vingadores - guerra infinita', 2018, 149)
    demolidor = Serie('Demolidor', 2016, 3)
    monstro_pantano = Serie('monstro do pantano', 2019, 1)
    sobrenatural = Serie('Sobrenatural', 2006, 15)

    hercules_disney.dar_like()
    hercules_disney.dar_like()
    hercules_disney.dar_like()
    hercules_disney.dar_like()
    homem_aranha_svpc.dar_like()
    homem_aranha_svpc.dar_like()
    homem_aranha_svpc.dar_like()
    homem_aranha_svpc.dar_like()
    homem_aranha_svpc.dar_like()
    homem_de_ferro.dar_like()
    homem_de_ferro.dar_like()
    homem_de_ferro.dar_like()
    homem_de_ferro.dar_like()
    homem_de_ferro.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    sobrenatural.dar_like()
    sobrenatural.dar_like()
    sobrenatural.dar_like()
    sobrenatural.dar_like()
    monstro_pantano.dar_like()
    monstro_pantano.dar_like()
    monstro_pantano.dar_like()

    filmes_e_serie = [vingadores, monstro_pantano, hercules_disney, homem_aranha_svpc, homem_de_ferro, demolidor,sobrenatural]

    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_serie)

    for programa in playlist_fim_de_semana:
        print(programa)

    print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

    print(f'Ta ou nao ta? {demolidor in playlist_fim_de_semana}')