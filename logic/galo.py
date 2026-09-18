class Galo:
    def __init__(self, nome, hp_max, ataque, defesa, caminho_imagem):
        self.nome = nome
        self.nivel = 1
        self.xp = 0
        self.hp_max = hp_max
        self.hp_atual = hp_max
        self.ataque = ataque
        self.defesa = defesa
        self.caminho_imagem = caminho_imagem