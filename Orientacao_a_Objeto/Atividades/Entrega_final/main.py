from mes import Mes
from dia import Dia
from sala1 import Sala1
from sala2 import Sala2
from sala3 import Sala3
from sala4 import Sala4
from horario import Horario
from cadastroSocio import CadastrarSocio
from secretaria import Secretaria
from reserva import Reserva

# Classes sócio e Sala, estão "inclusas" na classe Horario.
# Classe horario está "inclusa" na classe Dia
# Classe Dia está "inclusa" na classe Mes
# Todas as manipulações estão dentro da classe Reserva
# Dupla: Matheus Silva Da Costa, João Marcelo Beserra Silva

if __name__ == '__main__':
	reserva = Reserva()
	while True:
		print("\nDigite 1 e ENTER para cadastrar sócio e realizar da reserva de uma sala, associado ao nome do sócio que requisitante ")
		print("Digite 2 e ENTER para visualizar todas as reservas feitas")
		print("Digite 3 e ENTER para visualizar reservas feitas por um sócio")
		print("Digite 4 e ENTER para verificar se há reserva feita em uma sala dependendo do dia, horario e mês")
		print("Digite 5 e ENTER para alterar o nome do sócio da reserva")
		print("Digite 6 e ENTER para alterar o horário da reserva")
		print("Digite 7 e ENTER para verificar o número de lugares de um sala")
		print("Digite 8 e ENTER para remover uma reserva")
		print("Digite 9 e ENTER para verificar agendamentos de algum dia especifico")
		opcao = input(": \n")
		if opcao == "1":
			nomeSocio = str(input("Nome Sócio: "))
			socio = CadastrarSocio(nome = nomeSocio)
			salaEscolhida = str(input("Sala: 1/2/3/4: "))
			if salaEscolhida == "1":
				sala = Sala1() 
			elif salaEscolhida == "2":
				sala = Sala2() 
			elif salaEscolhida == "3":
				sala = Sala3() 
			elif salaEscolhida == "4":
				sala = Sala4()
			else:
				print("Sala não existente")	
			selecionar_horario = str(input("Digite o horario: (Horário de funcionamento das 08:00 as 22:00) "))	 
			horario = Horario(horario = selecionar_horario, socio = socio, sala = sala)
			data = int(input("Digite a data: "))
			dia = Dia(dia = data, horario = horario)
			nomeMes = str(input("Digite o nome do mês: "))
			reserva1 = Mes(nomeMes = nomeMes, dia = dia)
			id_reserva = reserva.id(dia = dia, mes = nomeMes)
			reserva.adicionar_reserva(reserva = reserva1, id = id_reserva)  # adicionar reserva
		elif opcao == "2":
			reserva.mostrarReservas()
		elif opcao == "3":	
			nome = str(input("Sócio a verificar: "))
			reserva.pesquisar_socio(nome)
		elif opcao == "4":
			sala = str(input("digite a sala: sala 1/sala 2/sala 3/sala 4 "))
			horario = str(input("digite o horario: "))
			dia = int(input("digite a data: "))
			mes = str(input("digite o nome do mes: "))
			reserva.salasLivres(sala = sala, horario = horario, dia = dia, mes = mes)  # Saber se uma sala está livre, dependendo do horario, dia, mes passado como argumento
		elif opcao == "5":
			nomeSocio = str(input("Digite o nome do sócio: "))
			id_reserva = int(input("digite o id da reserva que deseja alterar: "))
			reserva.alteracao_socio(nomeSocio = nomeSocio, id = id_reserva)	
		elif opcao == "6":
			novoHorario = str(input("Digite um novo horário: "))
			id_reserva = int(input("Digite o id da reserva que deseja alterar: "))
			reserva.alteracao_horario(horario = novoHorario, id = id_reserva)
		elif opcao == "7":
			sala = str(input("Digite qual sala deseja saber o número de lugares: sala 1/sala 2/sala 3/sala 4 "))
			reserva.lugares_salas(sala = sala)
		elif opcao == "8":
			id_reserva = int(input("Digite a id da reserva a remover: "))
			reserva.remover_reserva(id = id_reserva)
		elif opcao == "9":
			data = int(input("Digite a data: "))
			mes = str(input("Mês: "))
			reserva.mostrarReservas_diaEspecifico(dia = data, mes = mes)
		else:
			print("Opção inválida")		





























