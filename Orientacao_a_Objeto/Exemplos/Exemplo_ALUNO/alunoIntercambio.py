from aluno import Aluno

class AlunoIntercambio(Aluno):
	def __init__(self, nome: str = None,  endereco: object = None, turma: object = None, sexo: str = None, faculdadeOrigem: object = None, passaporte: int = None):
		super().__init__(nome, endereco, turma, sexo)
		self.__faculdadeOrigem = faculdadeOrigem
		self.__passaporte = passaporte

	def get_faculdadeOrigem(self):
		return self.__faculdadeOrigem

	def get_passaporte(self):
		return self.__passaporte	

	def set_faculdadeOrigem(self, faculdadeOrigem: str = None):
		self.__faculdadeOrigem = faculdadeOrigem

	def set_passaporte(self, passaporte: int = None):
		self.__passaporte = passaporte

	faculdadeOrigem = property(get_faculdadeOrigem, set_faculdadeOrigem)
	passaporte = property(get_passaporte, set_passaporte)			
