# main.py
import flet as ft
from database import init_db
from app_logic import display_contacts, add_contact

def main(page: ft.Page):
    page.title = "Contact Book"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    theme_switch = ft.Switch(label="Dark Mode")

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK 
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.LIGHT
        )
        page.update
    
    theme_switch.on_change =toggle_theme

    db_conn = init_db()

    name_input = ft.TextField(label="Name", width=350)
    phone_input = ft.TextField(label="Phone", width=350)
    email_input = ft.TextField(label="Email", width=350)

    inputs = (name_input, phone_input, email_input)

    contacts_list_view = ft.ListView(expand=1, spacing=10, auto_scroll=True)

    add_button = ft.ElevatedButton(
        text="Add Contact",
        on_click=lambda e: add_contact(page, inputs, contacts_list_view, db_conn)
    )
    
    page.add(
        ft.Column([
            ft.Row([
                ft.Text("Contact Book", size=20, weight=ft.FontWeight.BOLD),
                theme_switch
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Text("Enter Contact Details:", size=20, weight=ft.FontWeight.BOLD),
            name_input,
            phone_input,
            email_input,
            add_button,
            ft.Divider(),
            ft.Text("Contacts:", size=20, weight=ft.FontWeight.BOLD),
            contacts_list_view,
            ]
        )
    )

    display_contacts(page, contacts_list_view, db_conn)


   
if __name__ == "__main__":
    ft.app(target=main)