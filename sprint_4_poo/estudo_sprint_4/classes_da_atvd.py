class Carro(): # Classe Principal 
    def  __init__(self, nome, modelo, ano, km): 
        
        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.km = km

    def exibir_dados(self, novo_analise):
        print(f"Modelo {self.modelo}\nAno {self.ano}")

        if self.ano < novo_analise:
            print("Carro Antigo")

        else:
            print("Carro Novo")

    def mudar_km(self, novo_km):
        print(f"Km atualizado, De {self.km} para {novo_km}")
        self.km = novo_km

class carroEletrico(Carro): ## Subclasse de carro

    def __init__(self, nome, modelo, ano, km, vw, saude_da_bateria):
        super().__init__(nome, modelo, ano, km)
        self.vw = vw
        self.saude_da_bateria = saude_da_bateria

    def exibir_dados_eletricos(self):
        print(f"\nPara Eletricos: \nVw: {self.vw}\nSaude da bateria {self.saude_da_bateria}")

    def analise_da_bateria(self, min_bateria):
        saude_bateria = self.saude_da_bateria
        saude_bateria = int(saude_bateria[:-1])
        if saude_bateria >= min_bateria:
            print(f"Bateria do {self.nome} Saudavel! ")
        else:
            print(f"Bateria do {self.nome} Nao Saudavel! ")