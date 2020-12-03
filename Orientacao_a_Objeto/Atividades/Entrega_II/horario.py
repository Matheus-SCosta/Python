class Horario:
	def __init__(self, horario: str = None, funcionario: object = None, sala1: object = None, sala2: object = None, sala3: object = None, sala4: object = None) :
		self.__horario = horario
		self.__fucionario = funcionario
		self.__sala1 = sala1
		self.__sala2 = sala2
		self.__sala3 = sala3
		self.__sala4 = sala4

	def get_horario(self):
		return self.__horario

	def get_funcionario(self):
		return self.__funcionario

	def get_sala1(self):
		return self.__sala1

	def get_sala2(self):
		return self.__sala2

	def get_sala3(self):
		return self.__sala3

	def get_sala4(self):
		return self.__sala4			

	def set_horario(self, horario: str = None):
		self.__horario = horario

	def set_funcionario(self, funcionario: object = None):
		self.__funcionario = funcionario	

	def set_sala1(self, sala1: object = None):	
		self.__sala1 = sala1 	

	def set_sala2(self, sala2: object = None):	
		self.__sala2 = sala2 	

	def set_sala3(self, sala3: object = None):	
		self.__sala3 = sala3 

	def set_sala4(self, sala4: object = None):	
		self.__sala4 = sala4			

	horario = property(get_horario, set_horario)
	funcionario = property(get_funcionario, set_funcionario)
	sala1 = property(get_sala1, set_sala1)
	sala2 = property(get_sala2, set_sala2)
	sala3 = property(get_sala3, set_sala3)
	sala4 = property(get_sala4, set_sala4)
