class Galo:
    def __init__(self, nome, hp_max, ataque, defesa, caminho_imagem, nivel=1, xp=0): # Parâmetros nivel e xp adicionados
        self.nome = nome
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

    def ganhar_xp(self, quantidade): # Lógica de XP e Level Up
        self.xp += quantidade
        xp_necessario = self.nivel * 100
        while self.xp >= xp_necessario:
            self.xp -= xp_necessario
            self.nivel += 1
            self.hp_max += 10
            self.hp_atual = self.hp_max
            self.ataque += 2
            self.defesa += 1
            xp_necessario = self.nivel * 100

    def to_dict(self): # Serialização para JSON
        return {
            "nome": self.nome,
            "hp_max": self.hp_max,
            "ataque": self.ataque,
            "defesa": self.defesa,
            "caminho_imagem": self.caminho_imagem,
            "nivel": self.nivel,
            "xp": self.xp
        }

    @classmethod
    def from_dict(cls, data): # Desserialização do JSON
        return cls(data["nome"], data["hp_max"], data["ataque"], data["defesa"], data["caminho_imagem"], data.get("nivel", 1), data.get("xp", 0))