import flet as ft

def criar_tela_perfil(jogador):
    if jogador.galo_ativo:
        galo = jogador.galo_ativo
        info_galo = ft.Card(
            content=ft.Container(
                padding=20,
                content=ft.Column([
                    ft.Image(src=galo.caminho_imagem, width=150, height=150),
                    ft.Text(f"{galo.nome} - Nível {galo.nivel}", weight=ft.FontWeight.BOLD, size=20),
                    ft.ProgressBar(value=galo.hp_atual/galo.hp_max, color=ft.Colors.RED, width=200),
                    ft.Text(f"HP: {galo.hp_atual}/{galo.hp_max} | ATQ: {galo.ataque} | DEF: {galo.defesa}")
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )
        )
    else:
        info_galo = ft.Text("Nenhum galo equipado.")

    return ft.Column([
        ft.Text(f"Perfil de {jogador.nome}", size=30, weight=ft.FontWeight.BOLD),
        ft.Text(f"Moedas: {jogador.moedas}", size=20, color=ft.Colors.AMBER),
        ft.Divider(),
        ft.Text("Galo Ativo:", size=24),
        info_galo
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)