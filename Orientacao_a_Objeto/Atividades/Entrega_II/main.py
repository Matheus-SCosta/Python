from mes import Mes
from dia import Dia
from sala1 import Sala1
from sala2 import Sala2
from sala3 import Sala3
from sala4 import Sala4
from horario import Horario
from teste import Teste
from socio import Socio
from secretaria import Secretaria

# Classes Funcionários, Sala1, Sala2, Sala3, Sala4 estão "inclusos" na classe Horario.
# Classe horario está "inclusa" na classe Dia
# Classe Dia está "inclusa" na classe Mes
# Todas as chamadas estão dentro da classe Teste
# Dupla: Matheus Silva Da Costa, João Marcelo Beserra Silva

if __name__ == '__main__':

	# atribuições classe Funcionario
	funcionario1 = Socio()   # Utilizei herança da classe funcionário
	funcionario1.nome = "Matheus Silva Da Costa" 
	funcionario1.ramal = 5631599	


	# atribuições classes Sala1, Sala2, Sala3, Sala4
	sala1 = Sala1(status = "Ocupada")
	sala2 = Sala2(status = "Ocupada")
	sala3 = Sala3(status = "Livre")
	sala4 = Sala4(status = "Livre")
	
	# atribuições classe Horario
	horario = Horario()
	horario.horario = "12:00 as 13:00"
	horario.funcionario = funcionario1 	# Object
	horario.sala1 = sala1 	# Object 
	horario.sala2 = sala2	# Object	
	horario.sala3 = sala3	# Object
	horario.sala4 = sala4	# Object

    # atribuição classe Dia
	dia1 = Dia()
	dia1.dia = 1
	dia1.horario = horario   # Object
	
	

	# atribuição classe Mês
	mes1 = Mes()
	mes1.mes = "Janeiro"
	mes1.dia = dia1    # Object
	

	# atribuição da classe de teste
	teste1 = Teste(mes1)
	print("Mês: ", teste1.mes)
	print("Dia: ", teste1.dia)
	print("Horario: ", teste1.horario)
	print("Sala 1: ", teste1.sala1)
	print("Sala 2: ", teste1.sala2)
	print("Sala 3: ", teste1.sala3)
	print("Sala 4: ", teste1.sala4)
	print("Funcionário: ", teste1.funcionario)
	print("Cargo: ", teste1.cargo)
	print("Ramal: ", teste1.ramal)


	
	




	



	

	



