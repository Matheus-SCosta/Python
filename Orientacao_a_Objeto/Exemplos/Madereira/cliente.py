# Informações do cliente

class Cliente:
	def __init__(self, nomeCliente: str = None):
		self.__nomeCliente = nomeCliente

	@property
	def mostrar_nomeCliente(self):
		return self.__nomeCliente

	@mostrar_nomeCliente.setter
	def atribuir_nomeCliente(self, novo_nomeCliente: str):
		self.__nomeCliente = novo_nomeCliente	

# Getter
	def get_nomeCliente(self):
		return self.__nomeCliente

# Setter
	def set_nomeCliente(self, novo_nomeCliente: str):
		self.__nomeCliente = novo_nomeCliente	
