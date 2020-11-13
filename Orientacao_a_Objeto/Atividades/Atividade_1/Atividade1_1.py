# 1.Crie uma classe Aluno com nome, matricula, endereço e cpf. Teste e exiba a informação dos alunos.




class Aluno:
	def __init__(self, nome: str = None, matricula: int = None, endereco: str = None, cpf: int = None):
		self.nome = nome
		self.matricula = matricula
		self.endereco = endereco
		self.cpf = cpf

	def atribuir_nome(self, nome: str = None):
		self.nome = nome

	def atribuir_matricula(self, matricula: int = None):
		self.matricula = matricula

	def atribuir_endereco(self, endereco: str = None):
		self.endereco = endereco

	def atribuir_cpf(self, cpf: int = None):
		self.cpf = cpf

	def exibir_todas_informacoes(self):
		return self.nome, self.matricula, self.endereco, self.cpf

if __name__ == 	'__main__':	
	aluno1 = Aluno()
	aluno1.atribuir_nome("Matheus Silva Da Costa")
	aluno1.atribuir_matricula(20182380033)
	aluno1.atribuir_endereco("Rua Aberlado Targino da Fonseca, Nº 626, Ernesto Geisel")
	aluno1.atribuir_cpf(11807248445)
	nome, matricula, endereco, cpf = aluno1.exibir_todas_informacoes()	
	print("Nome: ",nome)
	print("Matricula: ",matricula)
	print("Endereço: ",endereco)
	print("CPF: ",cpf)

