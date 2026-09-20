import flet as ft
from logic.galo import Galo
from logic.jogador import Jogador
from screens.perfil import criar_tela_perfil
from screens.rinha import criar_tela_rinha
from data.galos_db import GALOS_DB # Importado para podermos corrigir o save

def main(page: ft.Page):
    page.title = "Rinha Offline"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    meu_jogador = Jogador.carregar()
    
    # --- BLOCO DE CORREÇÃO DE SAVES ANTIGOS ---
    if meu_jogador and meu_jogador.galo_ativo:
        # 1. Se o nome for o antigo, atualizamos para o novo
        if meu_jogador.galo_ativo.nome == "Pintinho Inicial":
            meu_jogador.galo_ativo.nome = "Rooster Normal"
        
        # 2. Recalcula o HP máximo com a fórmula certa sempre que o jogo abre
        nome_galo = meu_jogador.galo_ativo.nome
        if nome_galo in GALOS_DB:
            hp_base = GALOS_DB[nome_galo]["hp_base"]
            nivel = meu_jogador.galo_ativo.nivel
            meu_jogador.galo_ativo.hp_max = hp_base + ((nivel - 1) * 12)
            
            # Se a vida atual for maior que a máxima, ajustamos
            if meu_jogador.galo_ativo.hp_atual > meu_jogador.galo_ativo.hp_max:
                meu_jogador.galo_ativo.hp_atual = meu_jogador.galo_ativo.hp_max
                
        meu_jogador.salvar()
    # ------------------------------------------

    if not meu_jogador:
        meu_jogador = Jogador("Henrique")
        meu_galo = Galo("Rooster Normal", 112, "assets/galos/00_2.png")
        meu_jogador.adicionar_galo(meu_galo)
        meu_jogador.salvar()

    tela_loja = ft.Text("Loja em construção...", size=30)
    conteudo_atual = ft.Container(content=criar_tela_perfil(meu_jogador))

    def mudar_aba(e):
        if e.control.selected_index == 0:
            conteudo_atual.content = criar_tela_perfil(meu_jogador)
        elif e.control.selected_index == 1:
            conteudo_atual.content = criar_tela_rinha(meu_jogador, page) 
        elif e.control.selected_index == 2:
            conteudo_atual.content = tela_loja
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.Icons.SPORTS_MMA, label="Treino"),
            ft.NavigationBarDestination(icon=ft.Icons.STORE, label="Loja"),
        ],
        on_change=mudar_aba
    )

    page.add(conteudo_atual)

ft.run(main)