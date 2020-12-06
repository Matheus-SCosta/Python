from abc import ABC, abstractmethod

class ContaBancaria(ABC):
	def __init__(self, numeroConta: int = None, saldo: float = None):
		self.__numeroConta = numeroConta
		self.__saldo = saldo

	def get_numeroConta(self):
		return self.__numeroConta

	def get_saldo(self):
		return self.__saldo

	def set_numeroConta(self, numeroConta: int = None):
		self.__numeroConta = numeroConta

	def set_saldo(self, saldo: float = None):
		self.__saldo = saldo

	@abstractmethod
	def sacar(self, valorSaque: float):
		pass

	@abstractmethod
	def depositar(self, valorDeposito: float):
		pass

	saldo = property(get_saldo, set_saldo)
	numeroConta = property(get_numeroConta, set_numeroConta)
