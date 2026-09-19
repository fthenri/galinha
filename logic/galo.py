import random # Nova importação
from data.galos_db import GALOS_DB # Nova importação

class Galo:
    def __init__(self, nome, hp_max, ataque, defesa, caminho_imagem, nivel=1, xp=0, tipo="Normal", skills_equipadas=None): # Parâmetro skills_equipadas adicionado
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel
        self.xp = xp
        self.hp_max = hp_max
        self.hp_atual = hp_max
        self.ataque = ataque
        self.defesa = defesa
        self.caminho_imagem = caminho_imagem
        self.skills_equipadas = skills_equipadas if skills_equipadas is not None else [] # Inicialização do array

    def obter_skills_desbloqueadas(self): # Novo método para checar habilidades do DB
        if self.nome not in GALOS_DB:
            return []
        skills_db = GALOS_DB[self.nome]["skills"]
        desbloqueadas = []
        for lvl, skill in skills_db.items():
            if lvl <= self.nivel:
                desbloqueadas.append((lvl, skill))
        return desbloqueadas

    def equipar_skills_bot(self): # Novo método para equipar as 5 mais fortes
        desbloqueadas = self.obter_skills_desbloqueadas()
        desbloqueadas.sort(key=lambda x: x[0], reverse=True)
        self.skills_equipadas = [skill for lvl, skill in desbloqueadas[:5]]

    def atacar(self): # Novo método para calcular dano e escolher skill
        if not self.skills_equipadas:
            self.equipar_skills_bot()
            
        if not self.skills_equipadas:
            return "Ataque Básico", self.ataque

        skill = random.choice(self.skills_equipadas)
        dano_base = random.randint(skill["min"], skill["max"])
        dano_total = dano_base + self.ataque
        return skill["nome"], dano_total

    def sofrer_dano(self, dano_recebido):
        dano_real = max(1, dano_recebido - self.defesa)
        self.hp_atual -= dano_real
        if self.hp_atual < 0:
            self.hp_atual = 0
        return dano_real

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        xp_necessario = 30 + (self.nivel - 1) * 60
        
        while self.xp >= xp_necessario:
            self.xp -= xp_necessario
            self.nivel += 1
            self.hp_max += 10
            self.hp_atual = self.hp_max
            self.ataque += 2
            self.defesa += 1
            xp_necessario = 30 + (self.nivel - 1) * 60

    def to_dict(self):
        return {
            "nome": self.nome,
            "tipo": self.tipo,
            "hp_max": self.hp_max,
            "ataque": self.ataque,
            "defesa": self.defesa,
            "caminho_imagem": self.caminho_imagem,
            "nivel": self.nivel,
            "xp": self.xp,
            "skills_equipadas": self.skills_equipadas # Inclusão no dicionário de save
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
            data.get("tipo", "Normal"),
            data.get("skills_equipadas", []) # Resgate do dicionário de save
        )