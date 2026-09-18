import flet as ft
import time # Importado para pausar os turnos
from logic.galo import Galo

def criar_tela_rinha(jogador):
    if not jogador.galo_ativo:
        return ft.Text("Equipe um galo no perfil primeiro!")

    meu_galo = jogador.galo_ativo
    inimigo = Galo("Galo Robô", 100, 12, 3, "assets/galos/010_2.png")
    
    meu_galo.hp_atual = meu_galo.hp_max # Recupera HP para o combate

    texto_log = ft.Text("A batalha começou!", size=14)
    
    texto_hp_meu = ft.Text(f"{meu_galo.hp_atual}/{meu_galo.hp_max}", size=12)
    barra_hp_meu = ft.ProgressBar(value=meu_galo.hp_atual/meu_galo.hp_max, color=ft.Colors.GREEN, width=150)
    
    texto_hp_inimigo = ft.Text(f"{inimigo.hp_atual}/{inimigo.hp_max}", size=12)
    barra_hp_inimigo = ft.ProgressBar(value=inimigo.hp_atual/inimigo.hp_max, color=ft.Colors.PURPLE, width=150) # Cor roxa igual ao Asura

    botao_atacar = ft.Button(content="Atacar")

    def atualizar_tela(e): # Renderiza novos valores
        texto_hp_meu.value = f"{meu_galo.hp_atual}/{meu_galo.hp_max}"
        barra_hp_meu.value = meu_galo.hp_atual / meu_galo.hp_max
        texto_hp_inimigo.value = f"{inimigo.hp_atual}/{inimigo.hp_max}"
        barra_hp_inimigo.value = inimigo.hp_atual / inimigo.hp_max
        e.page.update()

    def atacar(e):
        botao_atacar.disabled = True
        e.page.update()

        if meu_galo.hp_atual > 0 and inimigo.hp_atual > 0:
            dano_causado = inimigo.sofrer_dano(meu_galo.ataque)
            texto_log.value = f"Você usou Bico causando {dano_causado} de dano."
            atualizar_tela(e)
            
            time.sleep(1) # Simula o turno do oponente
            
            if inimigo.hp_atual > 0:
                dano_recebido = meu_galo.sofrer_dano(inimigo.ataque)
                texto_log.value = f"{texto_log.value}\nInimigo usou Arranhão causando {dano_recebido} de dano."
                atualizar_tela(e)
            else:
                xp_ganho, moedas_ganhas = 34, 6
                meu_galo.ganhar_xp(xp_ganho)
                jogador.moedas += moedas_ganhas
                jogador.salvar() # Grava a vitória no JSON
                texto_log.value = f"{texto_log.value}\n\nVocê venceu!\nDinheiro ganho: {moedas_ganhas}\nXP ganho: {xp_ganho}"
                atualizar_tela(e)
                return

            if meu_galo.hp_atual <= 0:
                texto_log.value = f"{texto_log.value}\n\nO seu galo foi derrotado..."
                atualizar_tela(e)
                return
        
        botao_atacar.disabled = False
        e.page.update()

    botao_atacar.on_click = atacar

    return ft.Column([
        ft.Text("Arena", size=30, weight=ft.FontWeight.BOLD),
        ft.Container(
            bgcolor=ft.Colors.BLACK_87,
            padding=15,
            border_radius=10,
            content=ft.Column([
                texto_log,
                ft.Divider(color=ft.Colors.GREY_800),
                ft.Row([
                    ft.Column([
                        ft.Text(f"{jogador.nome} Level {meu_galo.nivel}", weight=ft.FontWeight.BOLD),
                        texto_hp_meu,
                        barra_hp_meu
                    ]),
                    ft.Column([
                        ft.Text(f"{inimigo.nome} Level {inimigo.nivel}", weight=ft.FontWeight.BOLD),
                        texto_hp_inimigo,
                        barra_hp_inimigo
                    ])
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=10),
                ft.Image(src=inimigo.caminho_imagem, height=200, fit="contain") # Destaque na imagem inimiga
            ])
        ),
        botao_atacar
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)