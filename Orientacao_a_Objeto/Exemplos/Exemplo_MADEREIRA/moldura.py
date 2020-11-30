# Informações do tamanho da moldura e espessura

class Moldura:
	def __init__(self, altura: float = None, base: float = None, areaMoldura: float = None, espessura: float = None, areaEspessura: float = None):
		self.__altura = altura
		self.__base = base
		self.__espessura = espessura
		self.__areaEspessura = areaEspessura
		self.__areaMoldura = areaMoldura
 
	# Calculo área espessura
	def calculo_areaEspessura(self):
		altura = self.__altura
		largura = self.__base
		espessura = self.__espessura
		area: float = ((altura * espessura)*2) + ((largura-(espessura*2))*2)*2 
		self.atribuir_areaEspessura = area

	# Calculo area moldura
	def calculo_areaMoldura(self):
		altura: float = self.__altura - (self.__espessura*2)
		base: float = self.__base - (self.__espessura*2)
		area: float = base * altura
		self.atribuir_areaMoldura = area

	
	@property
	def mostrar_altura(self):
		return self.__altura

	@property
	def mostrar_base(self):
		return self.__base

	@property
	def mostrar_espessura(self):
		return self.__espessura	

	@property
	def mostrar_areaEspessura(self):
		return self.__areaEspessura	

	@property
	def mostrar_areaMoldura(self):
		return self.__areaMoldura			

	
	@mostrar_altura.setter
	def atribuir_altura(self, altura: float = None):
		self.__altura = altura

	@mostrar_base.setter
	def	atribuir_base(self, base: float = None):
		self.__base = base

	@mostrar_espessura.setter
	def atribuir_espessura(self, espessura: float = None):
		self.__espessura = espessura

	@mostrar_areaEspessura.setter
	def atribuir_areaEspessura(self, areaEspessura: float = None):
		self.__areaEspessura = areaEspessura	

	@mostrar_areaMoldura.setter
	def atribuir_areaMoldura(self, areaMoldura: float = None):
		self.__areaMoldura = areaMoldura		
	
	
# Getters
	def get_altura(self):
		return self.__altura
	
	def get_base(self):
		return self.__base

	def get_espessura(self):
		return self.__espessura

	def get_areaExpessura(self):
		return self.__areaEspessura

	def get_areaMoldura(self):
		return self.__areaMoldura
	
	
# Setters
	def set_altura(self, novaAltura: float):
		self.__altura = novaAltura

	def set_base(self, novaBase: float):
		self.__base = novaBase

	def set_espessura(self, novaEspessura: float):
		self.__espessura = novaEspessura

	def set_areaExpessura(self, novaAreaEspessura: float):
		self.__areaEspessura = novaAreaEspessura

	def set_areaMoldura(self, novaAreaMoldura: float):
		self.__areaMoldura = novaAreaMoldura						
