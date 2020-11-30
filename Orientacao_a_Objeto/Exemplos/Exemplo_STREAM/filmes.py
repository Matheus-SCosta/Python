from stream import Stream 

class Filme(Stream):
	def __init__(self, nome: str = None, ano: int = None, numeroLikes: int = None, duracao: str = None, data_preEstreia: str = None):
		super().__init__(nome, ano, numeroLikes)
		self.__duracao = duracao
		self.__preEstreia = data_preEstreia

	def set_duracao(self, duracao: str = None):
		self.__duracao = duracao

	def set_preEstreia(self, data_preEstreia: str = None):
		self.__preEstreia = data_preEstreia

	def get_duracao(self):
		return self.__duracao

	def get_preEstreia(self):
		return self.__preEstreia

	def data_preEstreia(self, data_preEstreia: str = None):
		if self.__preEstreia is not None:
			return f"Haverá pré-estreia no dia {self.__preEstreia}"
		return "Não haverá pré-estreia"	

	duracao = property(get_duracao, set_duracao)
	preEstreia = property(get_preEstreia, set_preEstreia)



