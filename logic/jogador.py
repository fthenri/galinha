import json
import os
from logic.galo import Galo

class Jogador:
    def __init__(self, nome, moedas=500): # Moedas como parâmetro opcional
        self.nome = nome
        self.moedas = moedas
        self.galos = []
        self.galo_ativo = None

    def adicionar_galo(self, galo):
        self.galos.append(galo)
        if self.galo_ativo is None:
            self.galo_ativo = galo

    def to_dict(self): # Serialização para JSON
        return {
            "nome": self.nome,
            "moedas": self.moedas,
            "galos": [galo.to_dict() for galo in self.galos],
            "galo_ativo_index": self.galos.index(self.galo_ativo) if self.galo_ativo else -1
        }

    @classmethod
    def carregar(cls, arquivo="save.json"): # Carrega estado salvo
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            jogador = cls(data["nome"], data.get("moedas", 500))
            for galo_data in data.get("galos", []):
                jogador.adicionar_galo(Galo.from_dict(galo_data))
            idx = data.get("galo_ativo_index", -1)
            if idx >= 0 and idx < len(jogador.galos):
                jogador.galo_ativo = jogador.galos[idx]
            return jogador
        return None

    def salvar(self, arquivo="save.json"): # Salva estado atual
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4)