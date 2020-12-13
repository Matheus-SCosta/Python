from sala1 import Sala1
from sala2 import Sala2
from sala3 import Sala3
from sala4 import Sala4

class Reserva:
	def __init__(self):
		self.__reserva = []
		self.__id = []
	
	def mostrarReservas(self):
		print("===================================================================\n")
		print("\nReservas: \n")
		for i in range(len(self.__reserva)):
			print("\nReserva", self.__id[i])
			print(f"Mês: {self.__reserva[i].mes} | Dia: {self.__reserva[i].dia.dia} | Horario: {self.__reserva[i].dia.horario.horario} | Sala: {self.__reserva[i].dia.horario.sala.sala} | Sócio: {self.__reserva[i].dia.horario.socio.nome}\n")
		print("===================================================================\n")

	# Realização da reserva de uma sala, associado ao nome do sócio que requisitou; (um sócio pode reservar uma sala por vez) 
	def adicionar_reserva(self, reserva: object, id: int or str = None):
		for i in range(len(self.__reserva)):
			if reserva.dia.horario.horario == self.__reserva[i].dia.horario.horario:  # Verificando se há alguma reserva no mesmo horario
				if reserva.dia.horario.sala.sala == self.__reserva[i].dia.horario.sala.sala: # na mesma sala
					if reserva.dia.dia == self.__reserva[i].dia.dia: # mesmo dia
						if reserva.mes == self.__reserva[i].mes: # mesmo mês
							print("Já há agendamento para essa sala, nesse horário, dia e mês")  # caso tenha reserva para o mesmo horário, sala, dia e mês não será feito a reserva
							return 
		self.__reserva.append(reserva)  # caso não tenha reserva para o mesmo horário, sala, dia e mês será feito a reserva
		self.__id.append(id)  # e o id 1será adicionado ao array id
		print(f"\nReserva {id} adicionada com sucesso")

	
	# Remoção da reserva feita pelo sócio;
	def remover_reserva(self, id = None):
		id = str(id)
		for i in range(len(self.__id)):
		
			if self.__id[i] == id:
				del(self.__id[i])
				del(self.__reserva[i])
				print(f"\nReserva {id} removida com sucesso")
				return
		print("Reserva não localizada")	

	
	#Pesquise sócio tem alguma reserva no dia; (o sócio pode fazer várias reservas ao longo do dia, desde que sejam em horários diferentes)a se aquel; 
	def pesquisar_socio(self, nomeSocio: str = None):
		quantidade_reservas = 0
		for i in range(len(self.__reserva)):
			if self.__reserva[i].dia.horario.socio.nome == nomeSocio:  # se houve reserva no nome do sócio 
				quantidade_reservas = quantidade_reservas + 1
		if quantidade_reservas == 0:  # se o sócio não tiver nenhuma reserva
			print("Socio não tem nenhuma reserva")
		print(f"\n{nomeSocio} possui {quantidade_reservas} reserva(as): \n")	
		for i in range(len(self.__reserva)): # mostrar reservas do socio
			if self.__reserva[i].dia.horario.socio.nome == nomeSocio:
				print(f"Reserva {self.__id[i]} \nMês: {self.__reserva[i].mes} | Dia: {self.__reserva[i].dia.dia} | Horario: {self.__reserva[i].dia.horario.horario} | Sala: {self.__reserva[i].dia.horario.sala.sala} | Sócio: {self.__reserva[i].dia.horario.socio.nome}")	

				

	
	# Alteração do nome do sócio na reserva pelo id da reserva ou pelo objeto reserva
	def alteracao_socio(self, nomeSocio: str = None, id: int = None):
		id = str(id)
		if id is not None:    
			for i in range(len(self.__id)):
				if self.__id[i] == id:
					self.__reserva[i].dia.horario.socio.nome = nomeSocio
					print("Alterado nome do sócio com sucesso")
					return
			print(f"Reserva {id} não localizada")			
			

	# Alteração de horário na reserva
	def alteracao_horario(self, horario: str = None, id: int = None):
		id = str(id)
		if id is not None:
			for i in range(len(self.__id)):
				if self.__id[i] == id:
					self.__reserva[i].dia.horario.horario = horario
					print("Alterado horário da reserva com sucesso")
					return
			print(f"Reserva {id} não localizada")		

	# Saber se a sala estará ocupada em determinado horário e data
	def salasLivres(self, sala: str = None, horario: str = None, dia: int = None, mes: str = None):
		for i in range(len(self.__reserva)):
			if self.__reserva[i].mes == mes:
				if self.__reserva[i].dia.dia ==	dia:
					if self.__reserva[i].dia.horario.horario == horario:
						if self.__reserva[i].dia.horario.sala.sala == sala:
							print(f"{sala} ocupada no horário das {horario} no dia {dia}/{mes} pelo sócio {self.__reserva[i].dia.horario.socio.nome}")
							return
		print(f"{sala} desocupada no horário das {horario} no dia {dia}/{mes}")

	
	# mostrar lugares de cada sala
	def lugares_salas(self, sala: str = None):
		if sala == "sala 1":
			sala1 = Sala1()
			print(f"Sala 1 tem {sala1.lugares} lugares")
		elif sala == "sala 2":
			sala2 = Sala2()
			print(f"Sala 2 tem {sala2.lugares} lugares")
		elif sala == "sala 3":
			sala3 = Sala3()
			print(f"Sala 3 tem {sala3.lugares} lugares")
		elif sala == "sala 4":
			sala4 = Sala4()
			print(f"Sala 4 tem {sala4.lugares} lugares")									
	
	# verificar se há reserva feita em determinada data e Mês
	def mostrarReservas_diaEspecifico(self, dia: int = None, mes: str = None):
		reservas_doDia = 0
		for i in range(len(self.__reserva)):
			if self.__reserva[i].mes == mes:
				if self.__reserva[i].dia.dia == dia:
					print("===================================================================\n")
					print("\nReservas:\n")
					print(f"\nReserva {self.__id[i]} \nMês: {self.__reserva[i].mes} | Dia: {self.__reserva[i].dia.dia} | Horario: {self.__reserva[i].dia.horario.horario} | Sala: {self.__reserva[i].dia.horario.sala.sala} | Sócio: {self.__reserva[i].dia.horario.socio.nome}")	
					reservas_doDia = reservas_doDia + 1
					print("===================================================================\n")
		if reservas_doDia == 0:
			print(f"\nNão há reservas feitas para {dia}/{mes}")		

	# gerar um ID para a Reserva
	def id(self, dia: int = None, mes: str = None):
		reserva_doDia = 0
		for i in range(len(self.__reserva)):
			if self.__reserva[i].mes == mes:
				if self.__reserva[i].dia.dia == dia.dia:	
					reserva_doDia = reserva_doDia + 1
		if mes == "janeiro":
			id_mes = 1
		elif mes == "fevereiro":
			id_mes = 2
		elif mes == "março":
			id_mes = 3
		elif mes == "abril":
			id_mes = 4
		elif mes == "maio":
			id_mes = 5
		elif mes == "junho":
			id_mes = 6
		elif mes == "julho":
			id_mes = 7
		elif mes == "agosto":
			id_mes = 8
		elif mes == "setembro":
			id_mes = 9
		elif mes == "outubro":
			id_mes = 10
		elif mes == "novembro":
			id_mes = 11
		elif mes == "dezembro":
			id_mes = 12

		id = (f"{dia.dia}{id_mes}{reserva_doDia}")
		return id

