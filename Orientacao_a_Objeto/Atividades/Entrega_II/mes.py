class Mes:
	def __init__(self, nomeMes: str = None, dia: object = None):
		self.__mes = nomeMes
		self.__dia = dia

	def get_mes(self):
		return self.__mes

	def get_dia(self):
		return self.__dia

	def set_mes(self, mes: str = None):
		self.__mes = mes

	def set_dia(self, dia: object = None):
		self.__dia = dia

	mes = property(get_mes, set_mes)
	dia = property(get_dia, set_dia)
