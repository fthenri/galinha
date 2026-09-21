import json
import os
from logic.galo import Galo

class Jogador:
    def __init__(self, nome, moedas=500, vel_rinha="1.0", dif_rinha="Facil"):
        self.nome = nome
        self.moedas = moedas
        self.vel_rinha = vel_rinha # Novo atributo
        self.dif_rinha = dif_rinha # Novo atributo
        self.galos = []
        self.galo_ativo = None

    def adicionar_galo(self, galo):
        self.galos.append(galo)
        if self.galo_ativo is None:
            self.galo_ativo = galo

    def to_dict(self):
        return {
            "nome": self.nome,
            "moedas": self.moedas,
            "vel_rinha": self.vel_rinha, # Salva configuração
            "dif_rinha": self.dif_rinha, # Salva configuração
            "galos": [galo.to_dict() for galo in self.galos],
            "galo_ativo_index": self.galos.index(self.galo_ativo) if self.galo_ativo else -1
        }

    @classmethod
    def carregar(cls, arquivo="save.json"):
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            jogador = cls(
                data["nome"], 
                data.get("moedas", 500),
                data.get("vel_rinha", "1.0"), # Resgata com fallback para saves antigos
                data.get("dif_rinha", "Facil")
            )
            for galo_data in data.get("galos", []):
                jogador.adicionar_galo(Galo.from_dict(galo_data))
            
            idx = data.get("galo_ativo_index", -1)
            if idx >= 0 and idx < len(jogador.galos):
                jogador.galo_ativo = jogador.galos[idx]
                
            return jogador
        return None

    def salvar(self, arquivo="save.json"):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4)