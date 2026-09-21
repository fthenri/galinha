import flet as ft

def main(page: ft.Page):
    page.title = "Flet Dropdown Test"
    
    col = ft.Column()
    
    for i in range(5):
        def on_change(e, slot=i):
            print(f"Dropdown {slot} changed to {e.control.value}")
            
        dd = ft.Dropdown(
            options=[ft.dropdown.Option("A"), ft.dropdown.Option("B"), ft.dropdown.Option("C")],
            on_change=on_change,
            value="A"
        )
        col.controls.append(dd)
        
    page.add(col)

ft.app(target=main)

