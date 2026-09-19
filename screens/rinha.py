import flet as ft
import asyncio
import random # Adicionado para sortear inimigos
from logic.galo import Galo

def criar_tela_rinha(jogador, page): 
    if not jogador.galo_ativo:
        return ft.Text("Equipe um galo no perfil primeiro!")

    meu_galo = jogador.galo_ativo
    inimigo = Galo("Galo Robô", 100, 12, 3, "assets/galos/010_2.png")
    
    meu_galo.hp_atual = meu_galo.hp_max 

    texto_log = ft.Text("Procurando oponente...", size=14)
    
    # UI extraída para variáveis para podermos alterar dinamicamente
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
        # Loop infinito para sequenciar as batalhas
        while arena.page is not None:
            # Sorteia um novo inimigo a cada ciclo
            imagens = [f"assets/galos/01{i}_2.png" for i in range(0, 9)] + ["assets/galos/00_2.png"]
            inimigo.nome = f"Selvagem {random.randint(1, 99)}"
            inimigo.caminho_imagem = random.choice(imagens)
            inimigo.hp_atual = inimigo.hp_max
            meu_galo.hp_atual = meu_galo.hp_max # Recupera a tua vida para a próxima luta
            
            texto_log.value = f"Um {inimigo.nome} apareceu!"
            atualizar_tela()
            
            vel = float(seletor_vel.value)
            await asyncio.sleep(vel)
            
            turno_jogador = True
            
            while meu_galo.hp_atual > 0 and inimigo.hp_atual > 0:
                if arena.page is None: 
                    return 

                vel = float(seletor_vel.value) 

                if turno_jogador:
                    dano = inimigo.sofrer_dano(meu_galo.ataque)
                    texto_log.value = f"➡️ {jogador.nome} usou Bico causando {dano} de dano"
                else:
                    dano = meu_galo.sofrer_dano(inimigo.ataque)
                    texto_log.value = f"{texto_log.value}\n⬅️ {inimigo.nome} usou Arranhão causando {dano} de dano"
                
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
                    texto_log.value = f"{texto_log.value}\n\n🏆 {jogador.nome} venceu!\n💰 +{moedas_ganhas} Moedas | ✨ +{xp_ganho} XP\nProcurando próximo..."
                    atualizar_tela()
                    await asyncio.sleep(float(seletor_vel.value) * 2) # Pausa antes de iniciar a próxima luta
                else:
                    texto_log.value = f"{texto_log.value}\n\n💀 O teu galo foi derrotado... Treino encerrado."
                    atualizar_tela()
                    break # Sai do loop infinito se perderes

    page.run_task(loop_batalha)

    return ft.Column([
        ft.Text("Treinamento", size=30, weight=ft.FontWeight.BOLD),
        seletor_vel,
        arena
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)