from Funcionarios.Classes.Junior import Junior
from Funcionarios.Classes.Pleno import Pleno
from Funcionarios.Classes.Senior import Senior

class Pessoa:
    def exibir(self):
        jose = Junior()
        jose.busca_perguntas_sem_resposta()
        jose.mostrar_tarefas()

        print('---')

        luan = Pleno()
        luan.busca_perguntas_sem_resposta()
        luan.busca_cursos_do_mes()
        luan.mostrar_tarefas()