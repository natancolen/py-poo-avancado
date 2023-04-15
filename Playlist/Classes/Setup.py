from Playlist.Classes.Serie import Serie
from Playlist.Classes.Filme import Filme
from Playlist.Classes.Playlist import Playlist

def gerar_likes_filmes(filme: Filme, total_likes: int):
    for like in range(total_likes):
        filme.dar_like()

def gerar_likes_series(serie: Serie, total_likes: int):
    for i in range(total_likes):
        serie.dar_like()

class FimDeSemana:
    aneis_do_poder = Serie('Aneis do poder', 2022, 1)
    hercules_disney = Filme('Hecules', 1997, 93)
    homem_aranha_svpc = Filme('homem aranha - sem volta para casa', 2022, 148)
    homem_de_ferro = Filme('Homem de Ferro', 2008, 126)
    vingadores = Filme('vingadores - guerra infinita', 2018, 149)
    demolidor = Serie('Demolidor', 2016, 3)
    monstro_pantano = Serie('monstro do pantano', 2019, 1)
    sobrenatural = Serie('Sobrenatural', 2006, 15)

    gerar_likes_filmes(hercules_disney, 4)
    gerar_likes_filmes(homem_aranha_svpc, 5)
    gerar_likes_filmes(homem_de_ferro, 5)
    gerar_likes_filmes(vingadores, 4)

    gerar_likes_series(demolidor, 4)
    gerar_likes_series(sobrenatural, 4)
    gerar_likes_series(monstro_pantano, 5)
    gerar_likes_series(aneis_do_poder, 3)
    def Exibir(self):
        filmes_e_serie = [self.vingadores, self.monstro_pantano, self.hercules_disney, self.homem_aranha_svpc, self.homem_de_ferro, self.demolidor, self.sobrenatural]

        playlist_fim_de_semana = Playlist('fim de semana', filmes_e_serie)

        for programa in playlist_fim_de_semana:
            print(programa)

        print(self.aneis_do_poder in playlist_fim_de_semana)

        print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')