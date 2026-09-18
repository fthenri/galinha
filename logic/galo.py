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

    def sofrer_dano(self, dano_recebido):
        dano_real = max(1, dano_recebido - self.defesa) 
        
        self.hp_atual -= dano_real
        
        if self.hp_atual < 0:
            self.hp_atual = 0
            
        return dano_real