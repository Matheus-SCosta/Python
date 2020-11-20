from tipoMadeira import Madeira
from moldura import Moldura
from preco import Preco
from cliente import Cliente


if __name__ == '__main__':

	# Valores pelos tipos de madeira
	print("============================================")
	print("TIPOS DE MADEIRA E VALORES POR METRO QUADRADO")
	print("============================================")
	valores_tipoMadeira = Madeira() 
	valor_Tipo1, valor_Tipo2, valor_Tipo3 = (valores_tipoMadeira.valoresTipos_deMadeira)
	print("Tipo 1: R${:.2f}".format(valor_Tipo1))
	print("Tipo 2: R${:.2f}".format(valor_Tipo2))
	print("Tipo 3: R${:.2f}".format(valor_Tipo3))

	print("============================================")
	print("ORÇAMENTO DE ACORDO COM ESCOLHAS DO CLIENTE")
	print("============================================")
	
	# Informações do cliente
	cliente = Cliente()
	nome = "Matheus Silva Da Costa"
	cliente.atribuir_nomeCliente = nome
	print("Cliente: ",cliente.mostrar_nomeCliente)

	# Cliente informa as medidas da moldura e espessura
	molduraRetangular = Moldura()
	molduraRetangular.atribuir_altura = 10
	molduraRetangular.atribuir_base = 30
	molduraRetangular.atribuir_espessura = 2
	molduraRetangular.calculo_areaEspessura()	
	molduraRetangular.calculo_areaMoldura()
	altura_daMoldura = molduraRetangular.mostrar_altura
	base_daMoldura = molduraRetangular.mostrar_base
	espessura_daMoldura = molduraRetangular.mostrar_espessura
	area_daEspessura = molduraRetangular.mostrar_areaEspessura
	area_daMoldura = molduraRetangular.mostrar_areaMoldura
	print("altura de moldura: {:.2f}cm".format(altura_daMoldura))
	print("Base da modulra: {:.2f}cm".format(base_daMoldura))
	print("Espessura da modulra: {:.2f}cm".format(espessura_daMoldura))
	print("Area da Espessura: {:.2f}cm".format(area_daEspessura))
	print("Area de Moldura: {:.2f}cm".format(area_daMoldura))


        # Cliente escolhe o tipo da madeira da moldura
	tipoMadeiraMoldura = Madeira()
	tipoMadeiraMoldura_valor, tipo_MadeiraMoldura  = tipoMadeiraMoldura.mostrar_tipo1
	print("Valor da Madeira para a moldura por metro quadrado: R${:.2f} - {}".format(tipoMadeiraMoldura_valor, tipo_MadeiraMoldura))

        # Cliente escolhe o tipo de madeira da espessura
	tipoMadeiraEspessura = Madeira()
	tipoMadeiraEspessura_valor, tipo_MadeiraEspessua  = tipoMadeiraEspessura.mostrar_tipo2
	print("Valor da Madeira para a Espessura por metro quadrado: R${:.2f} - {}".format(tipoMadeiraEspessura_valor, tipo_MadeiraEspessua))

        # Orçamento
	orcamento = Preco()
	orcamento.calcular_orcamento(area_daMoldura, tipoMadeiraMoldura_valor, area_daEspessura, tipoMadeiraEspessura_valor)
	orcamentoCompleto = orcamento.mostrar_orcamentoTotal
	orcamento_daMoldura = orcamento.mostrar_orcamentoMoldura
	orcamento_daEspessura = orcamento.mostrar_orcamentoEspessura
	print("Orcamento para moldura: R${:.2f}".format(orcamento_daMoldura))
	print("Orçamento para Espessura: R${:.2f}".format(orcamento_daEspessura))
	print("Orçamento total: R${:.2f}".format(orcamentoCompleto))
