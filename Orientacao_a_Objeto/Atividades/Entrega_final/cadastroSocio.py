class CadastrarSocio:
	def __init__(self, nome: str = None):
		self.__nome = nome

	def get_nome(self):
		return self.__nome		

	def set_nome(self, nome: str = None):
		self.__nome = nome
	
	nome = property(get_nome, set_nome)
