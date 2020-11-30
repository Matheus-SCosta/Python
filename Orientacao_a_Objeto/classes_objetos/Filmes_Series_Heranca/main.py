from filmes import Filme
from series import Serie





if __name__ == '__main__':
	BetterCallSaul = Serie()
	BetterCallSaul.nome = "Better Call Saul"
	BetterCallSaul.ano = 2015
	BetterCallSaul.numeroLikes = 96531546778912
	BetterCallSaul.temporadas = 5
	BetterCallSaul.spinoffs = "Breaking Bad"
	print("Série",BetterCallSaul.nome)
	print("Ano de estreia: ",BetterCallSaul.ano)
	print("Número de Likes: ",BetterCallSaul.numeroLikes)
	print("Temporadas: ",BetterCallSaul.temporadas)
	print(BetterCallSaul.spinoffs)
	print(BetterCallSaul.spinoff())

	print("\n=====================================\n")

	oCondeDe_MonteCristo = Filme()
	oCondeDe_MonteCristo.nome = "O conde de monte Cristo 2"
	oCondeDe_MonteCristo.ano = 2021
	oCondeDe_MonteCristo.numeroLikes = 541231448789456123123112134
	oCondeDe_MonteCristo.duracao = "2:14:00"
	print("Filme:",oCondeDe_MonteCristo.nome)
	print("Ano de estreia: ",oCondeDe_MonteCristo.ano)
	print("Número de likes: ",oCondeDe_MonteCristo.numeroLikes)
	print("Duração: ",oCondeDe_MonteCristo.duracao)
	print(oCondeDe_MonteCristo.data_preEstreia())
