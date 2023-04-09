class Filme():
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Serie():
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1

if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 149)
    monstro_pantano = Serie('monstro do pantano', 2019, 1)

    vingadores.dar_like()
    monstro_pantano.dar_like()
    monstro_pantano.dar_like()

    print(f'Filme: {vingadores.nome} - Ano: {vingadores.ano} - Duraçao: {vingadores.duracao} min - Likes: {vingadores.likes}')
    print(f'Serie: {monstro_pantano.nome} - Ano: {monstro_pantano.ano} - Temporadas: {monstro_pantano.temporadas} - Likes: {monstro_pantano.likes}')


