import flet as ft
from logic.galo import Galo
from logic.jogador import Jogador
from screens.perfil import criar_tela_perfil

def main(page: ft.Page):
    page.title = "Rinha Offline"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    meu_galo = Galo("Pintinho Inicial", 100, 15, 5, "assets/galos/00_2.png")
    meu_jogador = Jogador("Henrique")
    meu_jogador.adicionar_galo(meu_galo)

    tela = criar_tela_perfil(meu_jogador)
    page.add(tela)

ft.run(main)