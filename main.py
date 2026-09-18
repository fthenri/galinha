import flet as ft
from logic.galo import Galo
from logic.jogador import Jogador
from screens.perfil import criar_tela_perfil
from screens.rinha import criar_tela_rinha

def main(page: ft.Page):
    page.title = "Rinha Offline"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    meu_jogador = Jogador.carregar() # Tenta carregar o save
    if not meu_jogador: # Cria perfil inicial se não houver save
        meu_jogador = Jogador("Henrique")
        meu_galo = Galo("Pintinho Inicial", 100, 15, 5, "assets/galos/00_2.png")
        meu_jogador.adicionar_galo(meu_galo)
        meu_jogador.salvar()

    tela_loja = ft.Text("Loja em construção...", size=30)
    conteudo_atual = ft.Container(content=criar_tela_perfil(meu_jogador))

    def mudar_aba(e):
        if e.control.selected_index == 0:
            conteudo_atual.content = criar_tela_perfil(meu_jogador) # Atualiza dados na troca de aba
        elif e.control.selected_index == 1:
            conteudo_atual.content = criar_tela_rinha(meu_jogador) # Atualiza dados na troca de aba
        elif e.control.selected_index == 2:
            conteudo_atual.content = tela_loja
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.Icons.SPORTS_MMA, label="Rinha"),
            ft.NavigationBarDestination(icon=ft.Icons.STORE, label="Loja"),
        ],
        on_change=mudar_aba
    )

    page.add(conteudo_atual)

ft.run(main)