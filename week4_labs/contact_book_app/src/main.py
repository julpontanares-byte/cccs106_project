# main.py
import flet as ft
from database import init_db
from app_logic import display_contacts, add_contact

def main(page: ft.Page):
    # Page configuration
    page.title = "Contact Book"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    # Define toggle_theme function
    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        theme_switch.icon = (
            ft.Icons.SUNNY
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.Icons.DARK_MODE
        )
        theme_switch.update()
        page.update()

    theme_switch = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        tooltip="Toggle light/dark theme",
        icon_color=ft.Colors.AMBER,
        on_click=toggle_theme,
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            padding=10,
            bgcolor=ft.Colors.AMBER_100,
        ),
    )

    theme_switch.on_click = toggle_theme

    # Initialize database connection
    db_conn = init_db()

    # UI Elements
    name_input = ft.TextField(label="Name", width=350)
    phone_input = ft.TextField(label="Phone", width=350)
    email_input = ft.TextField(label="Email", width=350)

    inputs = (name_input, phone_input, email_input)

    # ListView to display contacts
    contacts_list_view = ft.ListView(
        expand=True, 
        spacing=10, 
        auto_scroll=False,
        height=300,
        on_scroll=ft.ScrollMode.ADAPTIVE
    )

    search_input = ft.TextField(
        label="Search by Name", 
        width=350,
        on_change=lambda e: display_contacts(
            page, contacts_list_view, db_conn, search_input.value
        ),
    )

    # Add Contact button
    add_button = ft.ElevatedButton(
        text="Add Contact",
        on_click=lambda e: add_contact(page, inputs, contacts_list_view, db_conn),
        width=350
    )
    
    # Layout
    page.add(
        ft.Column([
            ft.Row([
                    ft.Text("Contact Book", size=20, weight=ft.FontWeight.BOLD),
                    theme_switch
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
               width=350
            ),
            ft.Text("Enter Contact Details:", size=20, weight=ft.FontWeight.BOLD),
            name_input,
            phone_input,
            email_input,
            add_button,
            ft.Divider(),
            search_input,
            ft.Text("Contacts:", size=20, weight=ft.FontWeight.BOLD),
            contacts_list_view,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    display_contacts(page, contacts_list_view, db_conn)


   
if __name__ == "__main__":
    ft.app(target=main)