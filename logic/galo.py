import random
from data.galos_db import GALOS_DB

class Galo:
    def __init__(self, nome, hp_max, caminho_imagem, nivel=1, xp=0, tipo="Normal", skills_equipadas=None, efeitos=None): 
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel
        self.xp = xp
        self.hp_max = hp_max
        self.hp_atual = hp_max
        self.caminho_imagem = caminho_imagem
        self.skills_equipadas = skills_equipadas if skills_equipadas is not None else [] 
        self.efeitos = efeitos if efeitos is not None else {} 

    def obter_skills_desbloqueadas(self):
        if self.nome not in GALOS_DB:
            return []
        skills_db = GALOS_DB[self.nome]["skills"]
        desbloqueadas = []
        for lvl, skill in skills_db.items():
            if lvl <= self.nivel:
                desbloqueadas.append((lvl, skill))
        return desbloqueadas

    def equipar_skills_bot(self):
        desbloqueadas = self.obter_skills_desbloqueadas()
        desbloqueadas.sort(key=lambda x: x[0], reverse=True)
        self.skills_equipadas = [skill for lvl, skill in desbloqueadas[:5]]

    def atacar(self):
        if not self.skills_equipadas:
            self.equipar_skills_bot()
            
        if not self.skills_equipadas:
            return "Ataque Básico", 10, None

        skill = random.choice(self.skills_equipadas)
        dano_total = random.randint(skill["min"], skill["max"])
        efeito = skill.get("efeito", None)
        return skill["nome"], dano_total, efeito

    def aplicar_efeito(self, nome_efeito):
        duracoes = {
            "Bleeding": 3,
            "Hemorrhage": 3,
            "Origami": 1,
            "Stun": 1,
            "Shield": 2
        }
        if nome_efeito in duracoes:
            self.efeitos[nome_efeito] = duracoes[nome_efeito]

    def processar_efeitos_inicio_turno(self):
        mensagens = []
        pode_atacar = True
        efeitos_para_remover = []

        for efeito, turnos in self.efeitos.items():
            if turnos > 0:
                if efeito == "Bleeding":
                    dano = int(self.hp_max * 0.05) # 5% do HP Máximo
                    self.hp_atual -= dano
                    mensagens.append(f"{self.nome} perdeu {dano} HP por Bleeding.")
                elif efeito == "Hemorrhage":
                    dano = int(self.hp_max * 0.10) # 10% do HP Máximo
                    self.hp_atual -= dano
                    mensagens.append(f"{self.nome} perdeu {dano} HP por Hemorrhage.")
                elif efeito in ["Origami", "Stun"]:
                    pode_atacar = False
                    mensagens.append(f"{self.nome} está imobilizado ({efeito}) e perdeu o turno!")

                self.efeitos[efeito] -= 1
                if self.efeitos[efeito] <= 0:
                    efeitos_para_remover.append(efeito)

        for efeito in efeitos_para_remover:
            del self.efeitos[efeito]

        if self.hp_atual < 0:
            self.hp_atual = 0

        return mensagens, pode_atacar

    def sofrer_dano(self, dano_recebido):
        dano_real = max(1, dano_recebido)
        
        if self.efeitos.get("Shield", 0) > 0:
            dano_real = int(dano_real * 0.5) # Shield reduz dano pela metade
            self.efeitos["Shield"] -= 1
            if self.efeitos["Shield"] <= 0:
                del self.efeitos["Shield"]

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
            self.hp_max += 12
            self.hp_atual = self.hp_max
            xp_necessario = 30 + (self.nivel - 1) * 60

    def to_dict(self):
        return {
            "nome": self.nome,
            "tipo": self.tipo,
            "hp_max": self.hp_max,
            "caminho_imagem": self.caminho_imagem,
            "nivel": self.nivel,
            "xp": self.xp,
            "skills_equipadas": self.skills_equipadas,
            "efeitos": self.efeitos
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["nome"], 
            data["hp_max"], 
            data["caminho_imagem"], 
            data.get("nivel", 1), 
            data.get("xp", 0),
            data.get("tipo", "Normal"),
            data.get("skills_equipadas", []),
            data.get("efeitos", {})
        )