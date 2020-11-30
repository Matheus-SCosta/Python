# Informações sobre os valores de cada tipo de madeira

class Madeira:
	def __init__(self, valorTipo1: float = 20.00, valorTipo2: float = 15.00, valorTipo3: float = 40.00):
		self.__valorTipo1 = valorTipo1
		self.__valorTipo2 = valorTipo2
		self.__valorTipo3 = valorTipo3


	@property
	def mostrar_tipo1(self):
		return self.__valorTipo1, "Tipo de madeira 1"

	@property
	def mostrar_tipo2(self):
		return self.__valorTipo2, "Tipo de madeira 2"

	@property
	def mostrar_tipo3(self):
		return self.__valorTipo3, "Tipo de madeira 3"	

	@property
	def valoresTipos_deMadeira(self):
		return self.__valorTipo1, self.__valorTipo2, self.__valorTipo3
	
	
	@mostrar_tipo1.setter
	def atribuir_tipo1(self, novoValor_tipo1: float):
		self.__valorTipo1 = novoValor_tipo1

	@mostrar_tipo2.setter
	def atribuir_tipo2(self, novoValor_tipo2: float):
		self.__valorTipo2 = novoValor_tipo2

	@mostrar_tipo3.setter
	def atribuir_tipo3(self, novoValor_tipo3: float):
		self.__valorTipo3 = novoValor_tipo3
	
	
	
# Getters
	def get_tipo1(self):
		return self.__valorTipo1, "Tipo de madeira 1"

	def get_tipo2(self):
		return self.__valorTipo2, "Tipo de madeira 2"

	def get_tipo3(self):
		return self.__valorTipo3, "Tipo de madeira 3"
	
			
	

# Setters
	def set_tipo1(self, novoValor_tipo1: float):
		self.__valorTipo1 = novoValor_tipo1

	def set_tipo2(self, novoValor_tipo2: float):
		self.__valorTipo2 = novoValor_tipo2

	def set_tipo3(self, novoValor_tipo3: float):
		self.__valorTipo3 = novoValor_tipo3		
