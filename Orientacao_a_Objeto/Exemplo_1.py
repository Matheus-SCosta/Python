'''' 2.Modele uma classe funcionário. Ela deve ter o nome do funcionário, o departamento onde o mesmo trabalha, seu salário (float), a data de entrada no banco (str) e seu RG (str). Você deve criar alguns métodos de acordo com sua necessidade. Além deles, crie um método receberAumento(percentual_aumento: str) que aumenta o salário do funcionário de acordo com o parâmetro passado como argumento. 
Crie também um método chamado calcular_ganho_anual, que não recebe parâmetro algum, devolvendo o valor do salário multiplicado por 12. Por fim, crie uma aplicação teste para verificar sua classe. '''''

class Funcionario:
	def __init__(self, nome: str = None, departamento: str = None, salario: float = None, dataEntradaBanco: str = None, rg: str = None):
		self.nome = nome
		self.departamento = departamento
		self.salario = salario
		self.dataEntradaBanco = dataEntradaBanco
		self.rg = rg

	def atribuir_nome(self, nome: str = None):
		self.nome = nome

	def atribuir_departamento(self, departamento: str = None):
		self.departamento = departamento	

	def atribuir_salario(self, salario: float = None):
		self.salario = salario
	
	def atribuir_dataEntradaBanco(self, dataEntradaBanco: str = None):
		self.dataEntradaBanco = dataEntradaBanco

	def atribuir_rg(self, rg: str = None):
		self.rg = rg

	def exibir_informacoes(self):
		print("Nome funcionário: ",self.nome)
		print("Departamento: ", self.departamento)
		print("Salário: R${:.3f}".format(self.salario))
		print("Data de entrada no banco: ", self.dataEntradaBanco)
		print("Rg: ", self.rg)		 			

	def receberAumento(self, percentual_aumento: str = None):
		percentual_aumento = int(percentual_aumento)
		salario_atual = self.salario
		aumento = (salario_atual/100) * percentual_aumento
		self.atribuir_salario(salario_atual + aumento) 

	def calcular_ganho_anual(self):
		salario_atual = self.salario
		ganho_anual = salario_atual * 12
		return ganho_anual

func1 = Funcionario()
func1.atribuir_nome("Matheus Silva Da Costa")
func1.atribuir_departamento("TI")
func1.atribuir_dataEntradaBanco("25/03/2021")
func1.atribuir_rg("5.623.80")
func1.atribuir_salario(4.250)
func1.receberAumento("20")
func1.exibir_informacoes()
print("Ganho total anual: {:.3f}".format(func1.calcular_ganho_anual()))

print(" =================== ")
func2 = Funcionario()
func2.nome = "João Alberto Nunes"
func2.departamento = "Rh"
func2.salario = 1.520
func2.dataEntradaBanco = "14/05/2020"
func2.rg = "4.659-18"
func2.exibir_informacoes()
print("Ganho total anual: {:.3f}".format(func2.calcular_ganho_anual()))



