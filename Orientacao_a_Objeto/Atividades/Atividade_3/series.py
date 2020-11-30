from stream import Stream 

class Serie(Stream):
	def __init__(self, nome: str = None, ano: int = None, likes: int = None, temporadas: int = None, spinoffs: str = None):
		super().__init__(nome, ano, likes)
		self.__temporadas = temporadas
		self.__spinoffs = spinoffs  

	def set_temporadas(self, temporadas: int = None):
		self.__temporadas = temporadas

	def set_spinoffs(self, spinoffs: str = None):
		self.__spinoffs = spinoffs	

	def get_temporadas(self):
		return self.__temporadas

	def get_spinoffs(self):
		return self.__spinoffs

	def spinoff(self):
		if self.__spinoffs is not None:
			return f"Série é spinoff da série {self.__spinoffs}"
		return "Série não há spinoffs"


	temporadas = property(get_temporadas, set_temporadas)
	spinoffs = property(get_spinoffs, set_spinoffs)




