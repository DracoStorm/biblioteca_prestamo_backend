from datetime import date, timedelta
from .models import Student, Admin, Loan, Book, StudentLoans
from django.utils import timezone


# Acá va el MODELO, el que se encuentra en el diagrama, solo utiliza las clases de modelo para CONSULTAS


class Usuario():
    def buscarLibro(title: str):
        return Book.objects.filter(title__icontains=title)


class Estudiante(Usuario):
    def getPrestamo(self, r_est: int):
        return Student.objects.get(register=r_est).loans

    def renovarPrestamo(self, id_pres: int):
        pres = Loan.objects.get(id=id_pres)
        if pres.devolution_date <= timezone.now().date() or pres.renew_tries >= 2:
            raise Exception('Demasiadas renovaciones')
        pres.renew_tries += 1
        pres.devolution_date += timedelta(weeks=2)
        return pres


class Administrador(Usuario):

    def registrarEstudiante(self, reg_est: int, nombre: str, apellido: str, correo_e: str):
        est = Student.objects.create(
            register=reg_est, first_name=nombre, last_name=apellido, e_mail=correo_e, loans=StudentLoans.objects.create())
        est.save()

    def actualizarEstudiante(self, reg_est: int, nom_est: str | None, ape_est: str | None, e_ma_est: str | None):

        est = Student.objects.get(register=reg_est)

        allNone: bool = True
        if nom_est is not None:
            est.first_name = nom_est
            allNone = False
        if ape_est is not None:
            est.last_name = ape_est
            allNone = False
        if e_ma_est is not None:
            est.e_mail = e_ma_est
            allNone = False
        if allNone:
            raise Exception('All None values')
        est.save()

    def eliminarEstudiante(self, reg_est: int):
        Student.objects.filter(register=reg_est).delete()

    def registrarLibro(self, titulo: str, autor: str, editorial: str, categoria: str):
        lib = Book.objects.create(
            title=titulo, author=autor, editorial=editorial, category=categoria)
        lib.save()

    def actualizarLibro(self, reg_lib: int, titulo: str | None, autor=str | None):
        lib = Book.objects.get(id=reg_lib)
        allNone: bool = True
        if titulo is not None:
            lib.title = titulo
            allNone = False
        if autor is not None:
            lib.author = autor
            allNone = False
        if allNone:
            raise Exception('All None values')
        lib.save()

    def eliminarLibro(self, reg_lib: int):
        Book.objects.filter(id=reg_lib).delete()

    def estadoPrestamoEstudiante(self, reg_student: int):
        loan_student = Student.objects.select_related(
            "loans").get(register=reg_student)

    def agregarPrestamoEstudiante(self, reg_student: int, id_book: int, date_loan: str):

        libro = Book.objects.get(id=id_book)

        # creamos objeto Prestamo
        pres = Loan.objects.create(
            devolution_date=timezone.now().date()+timedelta(weeks=2), book=libro)
        pres.save()

        estudiante = Student.objects.get(register=reg_student)
        sl = estudiante.loans

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


class Prestamo():

    def getLoan_date(date_loan):
        loan_date = Loan.objects.get(loan_date=loan_date)
        return loan_date

    def getDevolution_date(dev_loan):
        loan_dev = Loan.objects.get(devolution_date=dev_loan)
        return loan_dev

    def getBook(book_loan):
        loan_book = Loan.objects.get(book=book_loan)
        return loan_book

    # Pendiente
    def renovarPrestamo():
        return


class Libro():
    # Pendiente Revision
    def __init__(self, reg_book, title_book, author_book, category_book, editorial_book):
        self.register = reg_book
        self.title = title_book
        self.author = author_book
        self.category = category_book
        self.editorial = editorial_book

    def getRegister(reg_book):
        book_reg = Book.objects.get(register=reg_book)
        return book_reg

    def getTitle(titl_book):
        book_titl = Book.objects.get(title=titl_book)
        return book_titl

    def getAthor(aut_book):
        book_aut = Book.objects.get(author=aut_book)
        return book_aut

    def getCategory(cate_book):
        book_cate = Book.objects.get(category=cate_book)
        return book_cate

    def getEditorial(edi_book):
        book_edi = Book.objects.get(editorial=edi_book)
        return book_edi

    def setRegister(re):
        Book.register = re

    def setTitle(ti):
        Book.title = ti

    def setAuthor(au):
        Book.author = au

    def setCategory(ca):
        Book.category = ca

    def setEditorial(ed):
        Book.editorial = ed
