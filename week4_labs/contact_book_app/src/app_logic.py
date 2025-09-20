# app_logic.py
import flet as ft
from database import update_contact_db, delete_contact_db, add_contact_db, get_all_contacts_db

def display_contacts(page, contacts_list_view, db_conn, search_term=""):
    """Fetches and displays all contacts (optionally filtered by search_term) in the ListView."""
    contacts_list_view.controls.clear()

    contacts = get_all_contacts_db(db_conn, search_term)  # <-- Pass search term here

    for contact in contacts:
        contact_id, name, phone, email = contact
        
        contact_card = ft.Card(
            elevation=3,
            margin=ft.margin.only(bottom=10),
            content=ft.Container(
                padding=15,
                border_radius=12,
                bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.ON_SURFACE),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(name, size=18, weight=ft.FontWeight.BOLD),
                                ft.PopupMenuButton(
                                    icon=ft.Icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(
                                            text="Edit",
                                            icon=ft.Icons.EDIT,
                                            on_click=lambda _, c=contact: open_edit_dialog(
                                                page, c, db_conn, contacts_list_view
                                            )
                                        ),
                                        ft.PopupMenuItem(),
                                        ft.PopupMenuItem(
                                            text="Delete",
                                            icon=ft.Icons.DELETE,
                                            on_click=lambda _, cid=contact_id: delete_contact(
                                                page, cid, db_conn, contacts_list_view
                                            )
                                        ),
                                    ],
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Row(
                            [
                                ft.Icon(ft.Icons.PHONE, size=16),
                                ft.Text(phone if phone else "N/A", selectable=True),
                            ],
                            spacing=5,
                        ),
                        ft.Row(
                            [
                                ft.Icon(ft.Icons.EMAIL, size=16),
                                ft.Text(email if email else "N/A", selectable=True),
                            ],
                            spacing=5,
                        ),
                    ],
                    spacing=8,
                ),
            ),
        )
        contacts_list_view.controls.append(contact_card)
    page.update()


def add_contact(page, inputs, contacts_list_view, db_conn):
    """Adds a new contact and refreshes the list."""
    name_input, phone_input, email_input = inputs
    name = name_input.value.strip()

    if not name:
        name_input.error_text = "Name cannot be empty"
        page.update()
        return
    else: 
        name_input.error_text = None 

    add_contact_db(db_conn, name_input.value, phone_input.value, email_input.value)
    
    for field in inputs:
        field.value = ""
        field.error_text = None

    display_contacts(page, contacts_list_view, db_conn)
    page.update()

def delete_contact(page, contact_id, db_conn, contacts_list_view):
    """Shows a confirmation dialog before deleting a contact."""

    def confirm_delete(e):
        # Perform deletion only if user confirms
        delete_contact_db(db_conn, contact_id)
        dialog.open = False
        page.update()
        display_contacts(page, contacts_list_view, db_conn)

    def cancel_delete(e):
        dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirm Delete"),
        content=ft.Text("Are you sure you want to delete this contact?"),
        actions=[
            ft.TextButton("Cancel", on_click=cancel_delete),
            ft.TextButton("Delete", on_click=confirm_delete),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.open(dialog)
    
def open_edit_dialog(page, contact, db_conn, contacts_list_view):
    """Opens a dialog to edit a contact's details."""
    contact_id, name, phone, email = contact
    edit_name = ft.TextField(label="Name", value=name)
    edit_phone = ft.TextField(label="Phone", value=phone)
    edit_email = ft.TextField(label="Email", value=email)

    def save_and_close(e):
        update_contact_db(db_conn, contact_id, edit_name.value, edit_phone.value, edit_email.value)
        dialog.open = False
        page.update()
        display_contacts(page, contacts_list_view, db_conn)

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Edit Contact"),
        content=ft.Column([edit_name, edit_phone, edit_email], tight=True, spacing=15),
        actions=[
            ft.TextButton("Cancel", on_click=lambda e: setattr(dialog, 'open', False)
    or page.update()),
            ft.TextButton("Save", on_click=save_and_close),
            ],
        actions_alignment=ft.MainAxisAlignment.END,
        )
    page.open(dialog)