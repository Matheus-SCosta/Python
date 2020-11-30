class Endereco:
	def __init__(self, rua: str = None, TipoMoradia: str = None, numero_CasaApartamento: int = None, pontoReferencia: str = None):
		self.__rua = rua
		self.__TipoMoradia = TipoMoradia
		self.__numero = numero_CasaApartamento
		self.__pontoReferencia = pontoReferencia

	def get_rua(self):
		return self.__rua

	def get_TipoMoradia(self):
		return self.__TipoMoradia

	def get_numero(self):
		return self.__numero

	def get_pontoReferencia(self):
		return self.__pontoReferencia

	def set_rua(self, rua: str = None):
		self.__rua = rua

	def set_TipoMoradia(self, TipoMoradia: str = None):
		self.__TipoMoradia = TipoMoradia

	def set_pontoReferencia(self, pontoReferencia: str = None):
		self.__pontoReferencia = pontoReferencia		

	def set_numero(self, numero_casaApartamento: int = None):
		self.__numero = numero_casaApartamento

	rua = property(get_rua, set_rua)
	TipoMoradia = property(get_TipoMoradia, set_TipoMoradia)
	pontoReferencia = property(get_pontoReferencia, set_pontoReferencia)
	numero = property(get_numero, set_numero)	
