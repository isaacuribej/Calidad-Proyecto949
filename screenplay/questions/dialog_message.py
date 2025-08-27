# screenplay/questions/dialog_message.py

from playwright.sync_api import Dialog
from screenplay.abilities.browse_the_web import BrowseTheWeb

class DialogMessage:
    @staticmethod
    def capture(actor) -> str:
        page = actor.ability_to(BrowseTheWeb).page
        dialog_text = {}

        def handle_dialog(dialog: Dialog):
            dialog_text["message"] = dialog.message
            dialog.dismiss()

        page.once("dialog", handle_dialog)
        return dialog_text
