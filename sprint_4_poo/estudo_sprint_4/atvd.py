from classes_da_atvd import Carro, carroEletrico

carro1 = Carro("mercedes", "GLA", 2006, "100100")
carro1.exibir_dados(2017)
print(f"km antes da troca: {carro1.km}")
carro1.mudar_km(200000)
print(f"km depois da troca: {carro1.km}")

carro2 = carroEletrico("BYD", "Seal", 2024, "23000", "200", "75%")
carro2.exibir_dados(2022)
carro2.exibir_dados_eletricos()
carro2.analise_da_bateria(70) ### % Min aceitavel