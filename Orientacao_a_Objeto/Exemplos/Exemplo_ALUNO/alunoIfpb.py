from aluno import Aluno

class AlunoIfpb(Aluno):
	def __init__(self, nome: str = None, endereco: object = None, turma: object = None, sexo: str = None, matricula: int = None):
		super().__init__(nome, endereco, turma, sexo)
		self.__matricula = matricula

	def get_matricula(self):
		return self.__matricula	

	def set_matricula(self, matricula: int = None):
		self.__matricula = matricula

	matricula = property(get_matricula, set_matricula)				
