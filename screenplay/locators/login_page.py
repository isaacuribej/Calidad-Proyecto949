# screenplay/locators/login_page.py

class LoginPage:
    PATH = "file:///C:/Users/User/Documents/New_Screening_System.html"
    
    CAMPO_ID = "#patientId"                  # input del ID del paciente
    CAMPO_EDAD = "#patientAge"               # input de Edad en años
    CAMPO_GENERO = "#patientGender"          # dropdown select
    BOTON_INICIAR_EVALUACION = "button:has-text('Iniciar evaluación')"
