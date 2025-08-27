# test/test_login_failed.py

from screenplay.tasks.navigate_to import NavigateTo
from screenplay.tasks.login import IniciarEvaluacion
from screenplay.questions.dialog_message import DialogMessage
from screenplay.locators.login_page import LoginPage

def test_login_failed_shows_dialog(user):
    # Primero navegamos al HTML local
    user.attempts_to(
        NavigateTo(LoginPage.PATH),
    )

    # Configuramos la captura del dialog
    dialog_text = DialogMessage.capture(user)

    # Ejecutamos la acción con campos vacíos
    user.attempts_to(
        IniciarEvaluacion("", "", ""),  # dejamos todo vacío
    )

    # Verificamos que apareció el mensaje esperado
    assert dialog_text.get("message") == "Por favor complete todos los campos del paciente."
