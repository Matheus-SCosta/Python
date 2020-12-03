class Teste:
	def __init__(self, mes: object = None):
		self.__mes = mes

	def get_mes(self):
		return self.__mes.mes

	def get_dia(self):
		return self.__mes.dia.dia

	def get_horario(self):
		return self.__mes.dia.horario.horario

	def get_sala1(self):
		return self.__mes.dia.horario.sala1.status

	def get_sala2(self):
		return self.__mes.dia.horario.sala2.status

	def get_sala3(self):
		return self.__mes.dia.horario.sala3.status
	
	def get_sala4(self):
		return self.__mes.dia.horario.sala4.status		

	def get_funcionario(self):
		return self.__mes.dia.horario.funcionario.nome			

	def get_cargo(self):
		return self.__mes.dia.horario.funcionario.cargo
	
	def get_ramal(self):
		return self.__mes.dia.horario.funcionario.ramal			

	mes = property(get_mes)
	dia = property(get_dia)
	funcionario = property(get_funcionario)
	horario = property(get_horario)
	sala1 = property(get_sala1)
	sala2 = property(get_sala2)
	sala3 = property(get_sala3)
	sala4 = property(get_sala4)
	cargo = property(get_cargo)
	ramal = property(get_ramal)

					
