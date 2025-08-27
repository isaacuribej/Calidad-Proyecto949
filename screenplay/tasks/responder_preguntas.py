from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.locators.cuestionario_page import CuestionarioPage

class ResponderPregunta:
    def __init__(self, respuesta_texto):
        self.respuesta_texto = respuesta_texto

    def perform_as(self, actor):
        page = BrowseTheWeb.as_(actor).page
        # Disambiguate the locator
        page.get_by_role("button", name=self.respuesta_texto).first.click()

    @staticmethod
    def con_respuesta(respuesta_texto):
        return ResponderPregunta(respuesta_texto)