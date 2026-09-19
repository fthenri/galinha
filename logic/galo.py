class Galo:
    # Adicionado o parâmetro 'tipo' com valor padrão
    def __init__(self, nome, hp_max, ataque, defesa, caminho_imagem, nivel=1, xp=0, tipo="Normal"): 
        self.nome = nome
        self.tipo = tipo # Atributo tipo
        self.nivel = nivel
        self.xp = xp
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

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        # Nova fórmula: 30 de base + 60 por nível
        xp_necessario = 30 + (self.nivel - 1) * 60 
        
        while self.xp >= xp_necessario:
            self.xp -= xp_necessario
            self.nivel += 1
            self.hp_max += 10
            self.hp_atual = self.hp_max
            self.ataque += 2
            self.defesa += 1
            # Recalcula para caso ganhe XP suficiente para subir mais de um nível de uma vez
            xp_necessario = 30 + (self.nivel - 1) * 60 

    def to_dict(self):
        return {
            "nome": self.nome,
            "tipo": self.tipo, # Adicionado ao save
            "hp_max": self.hp_max,
            "ataque": self.ataque,
            "defesa": self.defesa,
            "caminho_imagem": self.caminho_imagem,
            "nivel": self.nivel,
            "xp": self.xp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["nome"], 
            data["hp_max"], 
            data["ataque"], 
            data["defesa"], 
            data["caminho_imagem"], 
            data.get("nivel", 1), 
            data.get("xp", 0),
            data.get("tipo", "Normal") # Carregado do save
        )