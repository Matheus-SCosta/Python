from contaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
	def __init__(self, numeroConta: int = None, saldo: float = None, taxaOperacao: float = None):
		super().__init__(numeroConta, saldo)
		self.__taxaOperacao = taxaOperacao

	def get_taxaOperacao(self):
		return self.__taxaOperacao

	def set_taxaOperacao(self, taxaOperacao = None):
		self.__taxaOperacao = taxaOperacao

	def sacar(self, valorSaque: float):
		if (self.saldo - (valorSaque + self.__taxaOperacao)) < 0:  # Caso o valor solicitado para saque + taxa de operação seja maior que o saldo disponível.
			print(f"Saldo insuficiente! impossivel realizar saque de R${valorSaque}!") 
			print(f"Saldo em Conta: R${self.saldo}")
			print(f"Lembre-se que ao sacar é descontado o valor de saque + taxa de operação de R${self.__taxaOperacao}, cujo poderá afetar saques com valores iguais ao saldo disponível. ")
			return
		self.saldo = self.saldo - (valorSaque + self.__taxaOperacao)  # O saque ocorrerá apenas quando a conta possuir saldo suficiente para o valor de saque + taxa de operação.

	def depositar(self, valorDeposito: float):
		self.saldo = self.saldo + (valorDeposito - self.__taxaOperacao)	

	def __str__(self):
		return f"Saldo: R${self.saldo} | Numero da conta: {self.numeroConta} | Taxa Operação: {self.__taxaOperacao}"


	taxaOperacao = property(get_taxaOperacao, set_taxaOperacao)



