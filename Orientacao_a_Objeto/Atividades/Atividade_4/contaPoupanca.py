from contaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
	def __init__(self, numeroConta: int = None, saldo: float = None, credito: float = None):
		super().__init__(numeroConta, saldo)
		self.__credito = credito

	def sacar(self, valorSaque: float):
		saldo = self.saldo
		credito = 0 - self.__credito
		if (saldo - valorSaque) < credito:
			print(f"Saldo indisponivel! impossível sacar R${valorSaque}")
			print(f"Saldo disponível: R${saldo}")
			print(f"Crédito disponível: R${self.__credito}\n")
			return
		self.saldo = self.saldo - valorSaque
		print("Novo saldo: ", self.saldo,"\n")


	def depositar(self, valorDeposito: float):
		self.saldo = self.saldo + valorDeposito

	def get_credito(self):
		return self.__credito

	def set_credito(self, credito: float = None):
		self.__credito = credito

	def __str__(self):
		return f"Saldo: R${self.saldo} | Numero da conta: {self.numeroConta} | Crédito: R${self.__credito}"

	credito = property(get_credito, set_credito)
