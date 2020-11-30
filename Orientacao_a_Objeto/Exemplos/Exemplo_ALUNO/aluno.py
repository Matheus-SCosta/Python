class Aluno:
	def __init__(self, nome: str = None, endereco: object = None, turma: str = None, sexo: str = None):
		self.__nome = nome
		self.__endereco = endereco
		self.__turma = turma
		self.__sexo = sexo

	def get_nome(self):
		return self.__nome

	def get_endereco(self):
		return self.__endereco

	def get_turma(self):
		return self.__turma

	def get_sexo(self):
		return self.__sexo

	def set_nome(self, nome: str = None):
		self.__nome = nome

	def set_endereco(self, endereco: object = None):
		self.__endereco = endereco

	def set_matriculaAlunoTurma(self, turma: str = None):
		self.__turma = turma

	def set_sexo(self, sexo: str = None):
		self.__sexo = sexo									

	nome = property(get_nome, set_nome)
	endereco = property(get_endereco, set_endereco)
	turma = property(get_turma, set_matriculaAlunoTurma)
	sexo = property(get_sexo, set_sexo)

