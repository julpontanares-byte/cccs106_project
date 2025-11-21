import flet as ft
import mysql.connector
from mysql.connector import Error
from db_connection import connect_db

# Main function fro Flet app
def main(page: ft.Page):
    # -- Page Setup --
    page.title = "User Login"
    page.window.center()
    page.window.frameless = True
    page.window.height = 350
    page.window.width = 400
    page.bgcolor = ft.Colors.AMBER_ACCENT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- UI CONTROLS ---
    login_title = ft.Text(
        value="User Login",
        size=20,
        weight=ft.FontWeight.BOLD,
        font_family="Arial",
        text_align=ft.TextAlign.CENTER,
    )

    # Username input field
    username_row = ft.Row(
        controls=[
            ft.Icon(ft.Icons.PERSON_ROUNDED, size=30, color=ft.Colors.BLACK),
            ft.TextField(
                label="User name",
                hint_text="Enter your user name",
                helper_text="This is your unique identifier",
                width=250,
                autofocus=True,
                bgcolor=ft.Colors.LIGHT_BLUE_ACCENT,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # Password input field
    password_row = ft.Row(
        controls=[
            ft.Icon(ft.Icons.PASSWORD, size=30, color=ft.Colors.BLACK),
            ft.TextField(
                label="Password",
                hint_text="Enter your password",
                helper_text="This is your secret key",
                width=250,
                password=True,
                can_reveal_password=True,
                bgcolor=ft.Colors.LIGHT_BLUE_ACCENT,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # -- Overlay Container --
    # This is an overlay popup for Login successful, failed, Input error, and  Database error messages
    overlay = ft.Container(
        visible=False,
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        padding=20,
        margin=20,
        alignment=ft.alignment.center,
        content=ft.Column(
            [
                ft.Icon(name=ft.Icons.INFO, size=40, color=ft.Colors.WHITE),
                ft.Text("", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text("", size=18, text_align=ft.TextAlign.CENTER),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Ok",
                            icon=ft.Icon(ft.Icons.CLOSE),
                            on_click=lambda e: close_overlay()
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
    )

    # Function to show overlay messages
    def show_overlay(title, message, icon, color):
        overlay.content.controls[0].name = icon
        overlay.content.controls[0].color = color
        overlay.content.controls[1].value = title
        overlay.content.controls[2].value = message
        overlay.bgcolor = ft.Colors.WHITE
        overlay.visible = True
        page.update()

    def close_overlay():
        overlay.visible = False
        page.update()

    # -- LOGIN LOGIC --
    async def login_click(e):
        if not username_row.controls[1].value.strip() or not password_row.controls[1].value.strip():
            show_overlay("Input Error", "Please enter username and password", ft.Icons.INFO_ROUNDED, color=ft.Colors.RED)
            return

        try:
            #  This connect it to the database
            conn = connect_db()
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s LIMIT 1"
            cursor.execute(query, (username_row.controls[1].value, password_row.controls[1].value))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            # Check login results
            if result:
                show_overlay("Login Successful", f"Welcome, {username_row.controls[1].value}!", ft.Icons.CHECK_CIRCLE, color=ft.Colors.LIGHT_GREEN)
            else:
                show_overlay("Login Failed", "Invalid username or password", ft.Icons.ERROR, color=ft.Colors.RED)

        except Error:
            show_overlay("Database Error", "An error occurred while connecting to the database", ft.Icons.WARNING, color=ft.Colors.AMBER_100)

    # Login button
    login_button = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.LOGIN, color=ft.Colors.BLACK),
                ft.Text("Login"),
            ],
            alignment="center",
            spacing=5
        ),
        width=100,
        on_click=login_click, 
    )
       
    
       
        
    # Add UI elements to the page using a Stack
    page.add(
        ft.Stack(  # Stack allows overlay on top of main page
            controls=[
                ft.Column(
                    [
                        login_title,
                        username_row,
                        password_row,
                        ft.Row([login_button], alignment=ft.MainAxisAlignment.END),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                overlay,  # <-- this will show above everything when visible=True
            ]
        )
    )

ft.app(main)
