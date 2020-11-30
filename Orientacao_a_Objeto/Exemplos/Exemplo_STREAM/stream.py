class Stream:
	def __init__(self, nome: str = None, ano: int = None, likes: int = None):
		self.__nome = nome
		self.__ano = ano
		self.__numeroLikes = likes

	def get_nome(self):
		return self.__nome

	def get_ano(self):
		return self.__ano

	def get_numeroLikes(self):
		return self.__numeroLikes

	def set_nome(self, nome : str = None):
		self.__nome = nome

	def set_ano(self, ano: int = None):
		self.__ano = ano

	def set_numeroLikes(self, likes: int = None):
		self.__numeroLikes = likes

	nome = property(get_nome, set_nome)
	ano = property(get_ano, set_ano)
	numeroLikes = property(get_numeroLikes, set_numeroLikes)
	
						


			
