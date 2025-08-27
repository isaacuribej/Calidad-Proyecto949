from screenplay.tasks.navigate_to import NavigateTo
from screenplay.tasks.login import IniciarEvaluacion
from screenplay.questions.dialog_message import DialogMessage
from screenplay.locators.login_page import LoginPage

def test_login_failed_with_negative_age(user):
    user.attempts_to(
        NavigateTo(LoginPage.PATH),
    )
    user.attempts_to(
        IniciarEvaluacion("1234A54", "-33", "M"),
    )
    dialog_text = DialogMessage.capture(user)
    assert dialog_text.get("message") == "Edad fuera de rango permitido."

def test_login_failed_with_too_high_age(user):
    user.attempts_to(
        NavigateTo(LoginPage.PATH),
    )
    user.attempts_to(
        IniciarEvaluacion("1234A54", "200", "M"),
    )
    dialog_text = DialogMessage.capture(user)
    assert dialog_text.get("message") == "Edad fuera de rango permitido."