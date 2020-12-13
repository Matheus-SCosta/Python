class Horario:
	def __init__(self, horario: str = None, socio: object = None, sala: object = None) :
		self.__horario = horario
		self.__socio = socio
		self.__sala = sala


	def get_horario(self):
		return self.__horario

	def get_socio(self):
		return self.__socio

	def get_sala(self):
		return self.__sala

	def set_horario(self, horario: str = None):
		self.__horario = horario

	def set_socio(self, socio: object = None):
		self.__socio = socio

	def set_sala(self, sala = None):
		self.__sala = sala

	horario = property(get_horario, set_horario)
	socio = property(get_socio, set_socio)
	sala = property(get_sala, set_sala)

