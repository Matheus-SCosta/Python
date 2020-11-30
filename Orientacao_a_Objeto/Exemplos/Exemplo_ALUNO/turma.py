class Turma:
	def __init__(self, nomeDisciplina: str = None, ano: float = None, turno: str = None):
		self.__nomeDisciplina = nomeDisciplina
		self.__ano = ano
		self.__turno = turno

	def get_nomeDisciplina(self):
		return self.__nomeDisciplina

	def get_ano(self):
		return self.__ano

	def get_turno(self):
		return self.__turno

	def set_nomeDisciplina(self, nomeDisciplina: str = None):
		self.__nomeDisciplina = nomeDisciplina

	def set_ano(self, ano: float = None):
		self.__ano = ano				

	def set_turno(self, turno: str = None):
		self.__turno = turno

	nomeDisciplina = property(get_nomeDisciplina, set_nomeDisciplina)
	ano = property(get_ano, set_ano)
	turno = property(get_turno, set_turno)

