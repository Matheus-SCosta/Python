class Sala3:
	def __init__(self, sala: str = "sala 3", lugares: int = 30):
		self.__sala = sala
		self.__lugares = lugares

	def get_sala(self):
		return self.__sala

	def get_lugares(self):
		return self.__lugares	

	def set_sala(self, sala = None):
		self.__sala = sala

	def set_lugares(self, lugares = None):
		self.__lugares = lugares	

	sala = property(get_sala, set_sala)	
	lugares = property(get_lugares, set_lugares)
