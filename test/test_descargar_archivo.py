from screenplay.tasks.navigate_to import NavigateTo
from screenplay.tasks.realizar_evaluacion import RealizarEvaluacion
from screenplay.locators.login_page import LoginPage
from screenplay.abilities.browse_the_web import BrowseTheWeb

def test_realizar_evaluacion(user):
    respuestas = [
        "Sí, se estableció",
        "Sí",
        "Sí estoy/está enfermo",
        "Sí",
        "Sí",
        "Sí",
        "Más de 5 años",
        "Sí",
        "Sí, he sido valorado",
        "No, no tengo estudios",
        "No estoy seguro",
        "No estoy seguro",
        "No estoy seguro",
        "No estoy seguro",
        "No estoy seguro"
    ]

    user.attempts_to(
        NavigateTo(LoginPage.PATH),
        RealizarEvaluacion.con_datos("A123456", "20", "M", respuestas)
    )

    # Validación final: Verificar que el texto "Porcentaje de riesgo" está presente
    page = user.abilities[BrowseTheWeb].page
    assert page.locator("div.score-display").locator("div:has-text('Porcentaje de riesgo')").is_visible(), "El texto 'Porcentaje de riesgo' no está visible en la página."

    # Manejar la ventana emergente al hacer clic en "Descargar reporte"
    def handle_dialog(dialog):
        assert dialog.message == "Reporte descargado.", "El mensaje de la ventana emergente no es correcto."
        dialog.dismiss()  # O usa dialog.accept() si necesitas aceptar el diálogo

    page.on("dialog", handle_dialog)
    page.get_by_role("button", name="Descargar reporte").click()