class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.moedas = 500 
        self.galos = []
        self.galo_ativo = None

    def adicionar_galo(self, galo):
        self.galos.append(galo)
        if self.galo_ativo is None:
            self.galo_ativo = galo