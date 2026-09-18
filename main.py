import flet as ft

def main(page: ft.Page):
    page.title = "Rinha Offline"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto_inicial = ft.Text("Bem-vindo à Rinha Offline!", size=30)
    
    page.add(texto_inicial)

ft.run(main)