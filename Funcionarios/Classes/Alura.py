from Funcionarios.Classes.Funcionario import Funcionario

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete')
    def busca_perguntas_sem_resposta(self, mes=None):
        print(f'Mostrando perguntas nao respondidas do forum')