class FaculdadeOrigem:
	def __init__(self, nomeFaculdade: str = None, cidade: str = None, estado: str = None, Pais: str = None, anoMatricula: int = None):
		self.__nomeFaculdade = nomeFaculdade
		self.__cidade = cidade
		self.__estado = estado
		self.__pais = Pais
		self.__anoMatricula = anoMatricula

	def get_nomeFaculdade(self):
		return self.__nomeFaculdade	

	def get_cidade(self):
		return self.__cidade

	def get_estado(self):
		return self.__estado	

	def get_pais(self):
		return self.__pais

	def get_anoMatricula(self):
		return self.__anoMatricula

	def set_nomeFaculdade(self, nomeFaculdade: str = None):
		self.__nomeFaculdade = nomeFaculdade				

	def set_cidade(self, cidade: str = None):
		self.__cidade = cidade

	def set_estado(self, estado: str = None):
		self.__estado = estado	

	def set_pais(self, pais: str = None):
		self.__pais = pais

	def set_anoMatricula(self, anoMatricula: int = None):
		self.__anoMatricula = anoMatricula						

	nomeFaculdade = property(get_nomeFaculdade, set_nomeFaculdade)
	cidade = property(get_cidade, set_cidade)
	estado = property(get_estado, set_estado)
	pais = property(get_pais, set_pais)
	anoMatricula = property(get_anoMatricula, set_anoMatricula)	
