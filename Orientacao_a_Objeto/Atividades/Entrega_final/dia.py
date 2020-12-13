class Dia:
	def __init__(self, dia: str = None, horario: object = None):
		self.__dia = dia
		self.__horario = horario
		
	def get_horario(self):
		return self.__horario
	
	def get_dia(self):
		return self.__dia						

	def set_horario(self, horario: object = None):
		self.__horario = horario

	def set_dia(self, dia: str = None):	
		self.__dia = dia

	dia = property(get_dia, set_dia)
	horario = property(get_horario, set_horario)
