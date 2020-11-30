from turma import Turma
from alunoIntercambio import AlunoIntercambio
from alunoIfpb import AlunoIfpb
from endereco import Endereco
from faculdadeOrigem import FaculdadeOrigem

if __name__ == '__main__':
	turma1 = Turma(nomeDisciplina = "Redes de Computadores", ano = 2018.2, turno = "Manhã")
	turma2 = Turma(nomeDisciplina = "Mestrado em Inteligência Artificial", ano = 2018.1, turno = "Manhã")

	aluno1 = AlunoIfpb()
	endereco_aluno1 = Endereco(rua = "Rua abelardo Targino da Fonseca", TipoMoradia = "Casa", numero_CasaApartamento = 77, pontoReferencia = "Prox ao condominio Rafael")
	aluno1.endereco = endereco_aluno1 #object
	aluno1.nome = "Matheus Silva da Costa"
	aluno1.matricula = 20182380033
	aluno1.turma = turma1 #object



	aluno3 = AlunoIntercambio()
	faculdadeOrigem_aluno3 = FaculdadeOrigem(nomeFaculdade = "Havard", cidade = "Cambridge", estado = "Massachusetts", Pais = "Estados Unidos", anoMatricula = 2015)
	aluno3.nome = "Luiz"
	aluno3.passaporte = 6532000005
	aluno3.turma = turma2
	aluno3.sexo = "Masculino"
	aluno3.faculdadeOrigem = faculdadeOrigem_aluno3 # Object


