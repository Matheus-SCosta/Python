from funcionario import Funcionario

class Socio(Funcionario):
	def __init__(self, nome: str = None, ramal: str = None, cargo: str = "Socio"):
		super().__init__(nome, ramal)
		self.__cargo = cargo

	def get_cargo(self):
		return self.__cargo		

	def set_cargo(self, cargo: str = None):
		self.__cargo = cargo
	
	cargo = property(get_cargo, set_cargo)
