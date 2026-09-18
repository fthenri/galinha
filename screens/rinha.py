import flet as ft
from logic.galo import Galo

def criar_tela_rinha(jogador):
    if not jogador.galo_ativo:
        return ft.Text("Equipe um galo no perfil primeiro!")

    meu_galo = jogador.galo_ativo
    inimigo = Galo("Galo Robô", 100, 12, 3, "assets/galos/010_2.png")

    texto_log = ft.Text("A batalha começou!", size=20, text_align=ft.TextAlign.CENTER)
    
    barra_hp_meu = ft.ProgressBar(value=meu_galo.hp_atual/meu_galo.hp_max, color=ft.Colors.GREEN, width=120)
    barra_hp_inimigo = ft.ProgressBar(value=inimigo.hp_atual/inimigo.hp_max, color=ft.Colors.RED, width=120)

    def atacar(e):
        if meu_galo.hp_atual > 0 and inimigo.hp_atual > 0:
            dano_causado = inimigo.sofrer_dano(meu_galo.ataque)
            log = f"Causou {dano_causado} de dano!\n"
            
            if inimigo.hp_atual > 0:
                dano_recebido = meu_galo.sofrer_dano(inimigo.ataque)
                log += f"Recebeu {dano_recebido} de dano!"
            else:
                log += "Venceu a rinha! +50 moedas."
                jogador.moedas += 50
                botao_atacar.disabled = True

            if meu_galo.hp_atual <= 0:
                log += "\nO seu galo foi derrotado..."
                botao_atacar.disabled = True

            texto_log.value = log
            barra_hp_meu.value = meu_galo.hp_atual / meu_galo.hp_max
            barra_hp_inimigo.value = inimigo.hp_atual / inimigo.hp_max
            e.control.page.update()

    botao_atacar = ft.Button(content="Atacar", on_click=atacar)

    return ft.Column([
        ft.Text("Arena", size=30, weight=ft.FontWeight.BOLD),
        ft.Row([
            ft.Column([
                ft.Text("Seu Galo", weight=ft.FontWeight.BOLD),
                ft.Image(src=meu_galo.caminho_imagem, width=100, height=100),
                barra_hp_meu
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Text(" VS ", size=30, weight=ft.FontWeight.BOLD),
            ft.Column([
                ft.Text("Inimigo", weight=ft.FontWeight.BOLD),
                ft.Image(src=inimigo.caminho_imagem, width=100, height=100),
                barra_hp_inimigo
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        texto_log,
        botao_atacar
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)