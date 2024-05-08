from modelo.modelo import Administrador
from modelo.models import *

a = Administrador(12)

a.registrarEstudiante('Juan', 'Perez', 'example@gmail.com', 199900001)

StudentLoans.objects.get(id=1).loan_0
