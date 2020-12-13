class Funcionario:
	def __init__(self, nome: str = None, ramal: str = None):
		self.__nome = nome
		self.__ramal = ramal

	def get_nome(self):
		return self.__nome

	def get_ramal(self):
		return self.__ramal			

	def set_nome(self, nome: str = None):
		self.__nome = nome		

	def set_ramal(self, ramal: int = None):	
		self.__ramal = ramal 

	nome = property(get_nome, set_nome)
	ramal = property(get_ramal, set_ramal)			
