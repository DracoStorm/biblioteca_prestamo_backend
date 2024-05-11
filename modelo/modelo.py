from datetime import date, timedelta
from enum import auto
import secrets
from .models import Category, Student, Admin, Loan, Book, StudentLoans, Editorial
from django.utils import timezone


# Acá va el MODELO, el que se encuentra en el diagrama, solo utiliza las clases de modelo para CONSULTAS


class Libro():
    # Pendiente Revision
    def __init__(self, id: int):
        try:
            self.__b = Book.objects.get(id=id)
        except:
            raise Exception('Failed to create the object')
        # Todos los atributos son obtenidos de la clase de consulta
        # self.__b.id
        # self.__b.title
        # self.__b.author
        # self.__b.category
        # self.__b.editorial

    def setTitulo(self, titulo: str):
        self.__b.title = titulo
        self.__b.save()

    def setAuthor(self, autor: str):
        self.__b.author = autor
        self.__b.save()

    def setCategory(self, categoria: int):
        self.__b.category = Category.objects.get(id=categoria)
        self.__b.save()

    def setEditorial(self, editorial: int):
        self.__b.editorial = Editorial.objects.get(id=editorial)
        self.__b.save()

    def getBook(self):
        return self.__b


class Prestamo():

    def __init__(self, id) -> None:
        try:
            self.__l = Loan.objects.get(id=id)
        except:
            raise Exception('Failed to create the object')
        # Todos los atributos son obtenidos de la clase de consulta
        # self.__l.id
        # self.__l.loan_date
        # self.__l.devolution_date
        # self.__l.renew_tries
        # self.__l.book

    def getFechaPrestamo(self):
        return self.__l.loan_date

    def getFechaDevolucion(self):
        return self.__l.devolution_date

    def getLibro(self):
        return self.__l.book

    def renovarPrestamo(self):
        if self.__l.devolution_date <= timezone.now().date() or self.__l.renew_tries >= 2:
            raise Exception('Demasiadas renovaciones')
        self.__l.renew_tries += 1
        self.__l.devolution_date += timedelta(weeks=2)
        self.__l.save()


class Usuario():
    def buscarLibro(self, title: str | None = None, autor: str | None = None, editorial: int | None = None, categoria: int | None = None):
        try:
            if title:
                b = Book.objects.filter(title__icontains=title)
            if autor:
                b = Book.objects.filter(author__icontains=autor)
            if editorial:
                b = Book.objects.filter(editorial=editorial)
            if categoria:
                b = Book.objects.filter(categoria=categoria)
        except Book.DoesNotExist:
            raise Exception('Book doesnt exist')
        return b


class Estudiante(Usuario):
    def __init__(self, token) -> None:
        super().__init__()
        try:
            self.__s = Student.objects.get(token=token)
        except:
            raise Exception('Failed to create the object')

    def getPrestamos(self):
        return self.__s.loans

    def renovarPrestamo(self, id_pres: int):
        sl = self.__s.loans
        fields = StudentLoans._meta.get_fields()
        for field in range(2, 12):
            f = getattr(sl, fields[field].name)
            if not f:
                raise Exception('Loan not found')
            elif f.id == id_pres:
                p = Prestamo(id_pres)
                p.renovarPrestamo()
                return Loan.objects.get(id=id_pres)
        raise Exception('Loan not found')


class Administrador(Usuario):
    def __init__(self, token: str) -> None:
        super().__init__()
        try:
            self.__a = Admin.objects.get(token=token)
        except:
            raise Exception('Failed to create the object')

    def buscarEstudiante(self, matricula: int | None = None, nombre: str | None = None, apellido: str | None = None):
        try:
            if matricula:
                s = Student.objects.filter(register__icontains=matricula)
            if nombre:
                s = Student.objects.filter(first_name__icontains=nombre)
            if apellido:
                s = Student.objects.filter(last_name__icontains=apellido)
        except Student.DoesNotExist:
            raise Exception('Student doesnt exist')
        return s

    def registrarEstudiante(self, reg_est: int, nombre: str, apellido: str, correo_e: str):
        est = Student.objects.create(
            register=reg_est, first_name=nombre, last_name=apellido, e_mail=correo_e, loans=StudentLoans.objects.create(), token=secrets.token_hex(20))
        est.save()
        return est

    def actualizarEstudiante(self, reg_est: int, nom_est: str | None = None, ape_est: str | None = None, e_ma_est: str | None = None):

        est = Student.objects.get(register=reg_est)

        allNone: bool = True
        if nom_est:
            est.first_name = nom_est
            allNone = False
        if ape_est:
            est.last_name = ape_est
            allNone = False
        if e_ma_est:
            est.e_mail = e_ma_est
            allNone = False
        if allNone:
            raise Exception('All None values')
        est.save()
        return est

    def eliminarEstudiante(self, reg_est: int):
        Student.objects.filter(register=reg_est).delete()

    def registrarLibro(self, titulo: str, autor: str, editorial: str, categoria: str):
        lib = Book.objects.create(
            title=titulo, author=autor, editorial=editorial, category=categoria)
        lib.save()
        return lib

    def actualizarLibro(self, id_lib: int, titulo: str | None = None, autor: str | None = None, editorial: int | None = None, categoria: int | None = None):
        lib = Libro(id_lib)
        allNone: bool = True
        if titulo:
            lib.setTitulo(titulo)
            allNone = False
        if autor:
            lib.setAuthor(autor)
            allNone = False
        if editorial:
            lib.setEditorial(editorial)
            allNone = False
        if categoria:
            lib.setCategory(categoria)
            allNone = False
        if allNone:
            raise Exception('All None values')
        lib.save()
        return lib

    def eliminarLibro(self, id_lib: int):
        Book.objects.filter(id=id_lib).delete()

    def estadoPrestamoEstudiante(self, id_est: int):
        return Student.objects.get(register=id_est).loans

    def agregarPrestamoEstudiante(self, reg_student: int, id_book: int):

        libro = Book.objects.get(id=id_book)

        # creamos objeto Prestamo
        pres = Loan.objects.create(
            devolution_date=timezone.now().date()+timedelta(weeks=2), book=libro)
        pres.save()

        estudiante = Student.objects.get(register=reg_student)
        sl = estudiante.loans

        fields = StudentLoans._meta.get_fields()
        for field in range(2, 12):
            f = getattr(sl, fields[field].name)

        if sl.loan_0 == None:
            sl.loan_0 = pres
        elif sl.loan_1 == None:
            sl.loan_1 = pres
        elif sl.loan_2 == None:
            sl.loan_2 = pres
        elif sl.loan_3 == None:
            sl.loan_3 = pres
        elif sl.loan_4 == None:
            sl.loan_4 = pres
        elif sl.loan_5 == None:
            sl.loan_5 = pres
        elif sl.loan_6 == None:
            sl.loan_6 = pres
        elif sl.loan_7 == None:
            sl.loan_7 = pres
        elif sl.loan_8 == None:
            sl.loan_8 = pres
        elif sl.loan_9 == None:
            sl.loan_9 = pres
        else:
            raise Exception('Student has the maximum allowed loans')
        sl.save()
        return sl

    def eliminarPrestamoEstudiante(self, reg_student: int, id_pres):
        sl = Student.objects.get(register=reg_student).loans

        if sl.loan_0.id == id_pres:
            sl.loan_0 = None
        elif sl.loan_1.id == id_pres:
            sl.loan_1 = None
        elif sl.loan_2.id == id_pres:
            sl.loan_2 = None
        elif sl.loan_3.id == id_pres:
            sl.loan_3 = None
        elif sl.loan_4.id == id_pres:
            sl.loan_4 = None
        elif sl.loan_5.id == id_pres:
            sl.loan_5 = None
        elif sl.loan_6.id == id_pres:
            sl.loan_6 = None
        elif sl.loan_7.id == id_pres:
            sl.loan_7 = None
        elif sl.loan_8.id == id_pres:
            sl.loan_8 = None
        elif sl.loan_9.id == id_pres:
            sl.loan_9 = None

        sl.save()
        Loan.objects.filter(id=id_pres).delete()
