# Orçamento, de acordo com a area e tipo de madeira

class Preco:
	def __init__(self, orcamentoTotal: float = None, orcamentoEspessura: float = None, orcamentoMoldura: float = None):
		self.__orcamentoTotal = orcamentoTotal
		self.__orcamentoEspessura = orcamentoEspessura
		self.__orcamentoMoldura = orcamentoMoldura

	# calcula os valores dos orcamentos
	def calcular_orcamento(self, area_moldura: float = None, valorMadeira_moldura: float = None, area_espessura: float = None, valorMadeira_espessura: float = None):	
		valorMoldura: float = (valorMadeira_moldura/100) * area_moldura
		valorEspessura: float = area_espessura * (valorMadeira_espessura/100)
		valorTotal: float = valorMoldura + valorEspessura
		self.atribuir_orcamentoMoldura = valorMoldura
		self.atribuir_orcamentoEspessura = valorEspessura
		self.atribuir_orcamentoTotal = valorTotal

	@property
	def mostrar_orcamentoTotal(self):
		return self.__orcamentoTotal

	@property
	def mostrar_orcamentoEspessura(self):
		return self.__orcamentoEspessura

	@property
	def mostrar_orcamentoMoldura(self):
		return self.__orcamentoMoldura

	@mostrar_orcamentoTotal.setter
	def atribuir_orcamentoTotal(self, novoOrcamentoTotal: float):
		self.__orcamentoTotal = novoOrcamentoTotal

	@mostrar_orcamentoEspessura.setter
	def atribuir_orcamentoEspessura(self, novoOrcamentoEspessura: float):
		self.__orcamentoEspessura = novoOrcamentoEspessura

	@mostrar_orcamentoMoldura.setter
	def atribuir_orcamentoMoldura(self, novoOrcamentoMoldura: float):
		self.__orcamentoMoldura = novoOrcamentoMoldura					


	
	
	
	# Getters
	def get_orcamentoTotal(self):
		return self.__orcamentoTotal

	def get_orcamentoEspessura(self):
		return self.__orcamentoEspessura

	def get_orcamentoMoldura(self):
		return self.__orcamentoMoldura

	
	# Setters
	def set_orcamentoTotal(self, novoOrcamentoTotal: float):
		self.__orcamentoTotal = novoOrcamentoTotal	

	def set_orcamentoEspessura(self, novoOrcamentoEspessura: float):
		self.__orcamentoEspessura = novoOrcamentoEspessura

	def set_orcamentoMoldura(self, novoOrcamentoMoldura: float):
		self.__orcamentoMoldura = novoOrcamentoMoldura		
