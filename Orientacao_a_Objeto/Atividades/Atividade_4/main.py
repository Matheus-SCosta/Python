from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca


if __name__ == "__main__":
	conta_corrente1 = ContaCorrente()
	conta_corrente1.saldo = 1000.00
	conta_corrente1.numeroConta = 236549
	conta_corrente1.taxaOperacao = 2.00      # taxa fixa cobrada a cada saque ou depósito
	conta_corrente1.sacar(700.00)
	conta_corrente1.depositar(500.00)
	print("Conta corrente 1: ", conta_corrente1)
	print("================================================================================ \n")


	conta_poupanca1 = ContaPoupanca(numeroConta = 252503, saldo = 47000.00, credito = 300.00)
	conta_poupanca1.sacar(47301.00)
	print("Conta poupança 1: ", conta_poupanca1)

