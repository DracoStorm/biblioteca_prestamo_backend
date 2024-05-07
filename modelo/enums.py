from enum import Enum

# Acá crean las listas de los campos definidos


class Editorial(Enum):
    C1 = 'Alfa Omega'
    C2 = 'Porrua'
    C3 = 'Fondo cultural'
    ...


class Category  (Enum):
    TERROR = 'Terror'
    FANTASIA = 'Fantasía'
    CS = 'Ciencias de la computación'
    QFB = 'Químico Farmaco-biología'
    ...
