class Veiculo:
    def __init__(self,modelo,fab):
        self.modelo = modelo
        self.data_fabricacao = fab

class Carro(Veiculo):
    def __init__(self,modelo,fab,chassi,portas):
        super().__init__(modelo,fab)
        self.__numero_chassi = chassi
        self.portas = portas
    def set_numero_chassi(self,chassi):
        self.__numero_chassi = chassi

    def get_numero_chasi(self):
        return self.__numero_chassi

class Aviao(Veiculo):
    def __init__(self,modelo,fab,mot,comp):
        super().__init__(modelo,fab)
        self.numero_motores = mot
        self.nome_companhia = comp

class Navio(Veiculo):
    def __init__(self,modelo,fab,nome,anc,pas):
        super().__init__(modelo,fab)
        self.__nome = nome
        self.numero_ancoras = anc
        self.capacidade_passageiros = pas
    def get_nome(self):
        return self.__nome

v1 = Veiculo('palio',2010)
print(v1.modelo,v1.data_fabricacao)

c1 = Carro('volvo',2015,'a888b098',4)
print(c1.portas,c1.get_numero_chasi())

a1 = Aviao('air200',2022,5,'latam')
print(a1.numero_motores,a1.modelo)

n1 = Navio('barco',2000,'mar azul',3,200)
print(n1.modelo)