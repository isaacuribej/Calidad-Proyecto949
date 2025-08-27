# screenplay/tasks/login.py

from screenplay.actor import Task
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.locators.login_page import LoginPage

class IniciarEvaluacion(Task):
    def __init__(self, patient_id: str = "", edad: str = "", genero: str = ""):
        self.patient_id = patient_id
        self.edad = edad
        self.genero = genero

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        if self.patient_id:
            page.fill(LoginPage.CAMPO_ID, self.patient_id)
        if self.edad:
            page.fill(LoginPage.CAMPO_EDAD, self.edad)
        if self.genero:
            page.select_option(LoginPage.CAMPO_GENERO, self.genero)

        # click en el botón
        page.click(LoginPage.BOTON_INICIAR_EVALUACION)
