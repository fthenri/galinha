import flet as ft
import asyncio
import random
from logic.galo import Galo
from data.galos_db import GALOS_DB # Importação do banco de galos

def criar_tela_rinha(jogador, page):
    if not jogador.galo_ativo:
        return ft.Text("Equipe um galo no perfil primeiro!")
        
    meu_galo = jogador.galo_ativo
    inimigo = Galo("Dummy", 100, 10, 5, "assets/galos/00_2.png")
    
    meu_galo.hp_atual = meu_galo.hp_max 
    texto_log = ft.Text("Procurando oponente...", size=14)
    
    texto_nome_meu = ft.Text(f"{jogador.nome} Level {meu_galo.nivel}", weight=ft.FontWeight.BOLD)
    texto_hp_meu = ft.Text(f"{meu_galo.hp_atual}/{meu_galo.hp_max}", size=12)
    barra_hp_meu = ft.ProgressBar(value=1.0, color=ft.Colors.GREEN, width=150)
    
    texto_nome_inimigo = ft.Text(f"{inimigo.nome} Level {inimigo.nivel}", weight=ft.FontWeight.BOLD)
    texto_hp_inimigo = ft.Text(f"{inimigo.hp_atual}/{inimigo.hp_max}", size=12)
    barra_hp_inimigo = ft.ProgressBar(value=1.0, color=ft.Colors.PURPLE, width=150)
    imagem_inimigo = ft.Image(src=inimigo.caminho_imagem, height=200, fit="contain")
    
    seletor_vel = ft.Dropdown(
        label="Velocidade do Treino",
        options=[
            ft.dropdown.Option("1.0", "1x (Normal)"),
            ft.dropdown.Option("0.5", "2x (Rápido)"),
            ft.dropdown.Option("0.1", "10x (Flash)")
        ],
        value="1.0",
        width=200
    )
    
    arena = ft.Container(
        bgcolor=ft.Colors.BLACK_87,
        padding=15,
        border_radius=10,
        content=ft.Column([
            texto_log,
            ft.Divider(color=ft.Colors.GREY_800),
            ft.Row([
                ft.Column([
                    texto_nome_meu,
                    texto_hp_meu,
                    barra_hp_meu
                ]),
                ft.Column([
                    texto_nome_inimigo,
                    texto_hp_inimigo,
                    barra_hp_inimigo
                ])
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Container(height=10),
            imagem_inimigo
        ])
    )

    def atualizar_tela():
        texto_nome_meu.value = f"{jogador.nome} Level {meu_galo.nivel}"
        texto_hp_meu.value = f"{meu_galo.hp_atual}/{meu_galo.hp_max}"
        barra_hp_meu.value = meu_galo.hp_atual / meu_galo.hp_max
        
        texto_nome_inimigo.value = f"{inimigo.nome} Level {inimigo.nivel}"
        texto_hp_inimigo.value = f"{inimigo.hp_atual}/{inimigo.hp_max}"
        barra_hp_inimigo.value = inimigo.hp_atual / inimigo.hp_max
        imagem_inimigo.src = inimigo.caminho_imagem
        try:
            page.update()
        except Exception:
            pass 

    async def loop_batalha():
        while arena.page is not None:
            # Sorteio do inimigo baseado no DB e nível do jogador
            nome_sorteado = random.choice(list(GALOS_DB.keys()))
            dados_inimigo = GALOS_DB[nome_sorteado]
            nivel_inimigo = max(1, meu_galo.nivel + random.randint(-1, 2))
            
            inimigo.nome = nome_sorteado
            inimigo.tipo = dados_inimigo["tipo"]
            inimigo.nivel = nivel_inimigo
            inimigo.hp_max = dados_inimigo["hp_base"] + (nivel_inimigo * 10)
            inimigo.hp_atual = inimigo.hp_max
            inimigo.ataque = 10 + (nivel_inimigo * 2)
            inimigo.defesa = 5 + nivel_inimigo
            inimigo.caminho_imagem = dados_inimigo["caminho_imagem"]
            
            inimigo.equipar_skills_bot() # Atualiza as 5 skills do inimigo
            
            meu_galo.hp_atual = meu_galo.hp_max 
            
            texto_log.value = f"Um {inimigo.nome} Lvl {inimigo.nivel} apareceu!"
            atualizar_tela()
            
            vel = float(seletor_vel.value)
            await asyncio.sleep(vel)
            
            turno_jogador = True
            
            while meu_galo.hp_atual > 0 and inimigo.hp_atual > 0:
                if arena.page is None: 
                    return 
                vel = float(seletor_vel.value)
                
                if turno_jogador:
                    nome_skill, dano_ataque = meu_galo.atacar() # Implementação do atacar()
                    dano_real = inimigo.sofrer_dano(dano_ataque)
                    texto_log.value = f"  {jogador.nome} usou {nome_skill} causando {dano_real} de dano"
                else:
                    nome_skill, dano_ataque = inimigo.atacar() # Implementação do atacar()
                    dano_real = meu_galo.sofrer_dano(dano_ataque)
                    texto_log.value = f"{texto_log.value}\n  {inimigo.nome} usou {nome_skill} causando {dano_real} de dano"
                            
                atualizar_tela()
                
                if turno_jogador:
                    await asyncio.sleep(vel / 2)
                else:
                    await asyncio.sleep(vel)
                
                turno_jogador = not turno_jogador

            if arena.page is not None:
                if meu_galo.hp_atual > 0:
                    xp_ganho, moedas_ganhas = 34, 6
                    meu_galo.ganhar_xp(xp_ganho)
                    jogador.moedas += moedas_ganhas
                    jogador.salvar()
                    texto_log.value = f"{texto_log.value}\n\n  {jogador.nome} venceu!\n  +{moedas_ganhas} Moedas |   +{xp_ganho} XP\nProcurando próximo..."
                    atualizar_tela()
                    await asyncio.sleep(float(seletor_vel.value) * 2) 
                else:
                    texto_log.value = f"{texto_log.value}\n\n  O teu galo foi derrotado... Treino encerrado."
                    atualizar_tela()
                    break 

    page.run_task(loop_batalha)

    return ft.Column([
        ft.Text("Treinamento", size=30, weight=ft.FontWeight.BOLD),
        seletor_vel,
        arena
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)