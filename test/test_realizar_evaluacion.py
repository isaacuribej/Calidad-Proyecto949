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