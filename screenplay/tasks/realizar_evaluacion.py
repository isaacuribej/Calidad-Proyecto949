from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.locators.login_page import LoginPage
from screenplay.locators.cuestionario_page import CuestionarioPage
from screenplay.tasks.responder_preguntas import ResponderPregunta

class RealizarEvaluacion:
    def __init__(self, paciente_id, edad, genero, respuestas):
        self.paciente_id = paciente_id
        self.edad = edad
        self.genero = genero
        self.respuestas = respuestas  # lista de strings con textos de los botones

    def perform_as(self, actor):
        page = BrowseTheWeb.as_(actor).page

        # 1. Llenar datos del paciente
        page.fill(LoginPage.CAMPO_ID, self.paciente_id)
        page.fill(LoginPage.CAMPO_EDAD, self.edad)
        page.select_option(LoginPage.CAMPO_GENERO, self.genero)

        # 2. Iniciar evaluación
        page.click(LoginPage.BOTON_INICIAR_EVALUACION)

        # 3. Iterar sobre las respuestas
        for respuesta in self.respuestas:
            actor.attempts_to(
                ResponderPregunta.con_respuesta(respuesta)
            )

        # 4. Calcular resultado final
        page.click(CuestionarioPage.BOTON_CALCULAR_RESULTADO)

    @staticmethod
    def con_datos(paciente_id, edad, genero, respuestas):
        return RealizarEvaluacion(paciente_id, edad, genero, respuestas)
