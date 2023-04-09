class Filme():
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie():
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

if __name__ == '__main__':
    vingadores = Filme('Vingadores - Guerra Infinita', 2018, 149)
    monstro_pantano = Serie('Monstro do pantano', 2019, 1)

    print(f'Filme: {vingadores.nome} do ano {vingadores.ano} com o tempo de duraçao {vingadores.duracao} min ')
    print(f'Serie: {monstro_pantano.nome} do ano {monstro_pantano.ano} com o total de {monstro_pantano.temporadas} temporadas')


