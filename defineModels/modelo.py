from typing import Any
from .models import Student,Admin,Loan,Book
 

# Acá va el MODELO, el que se encuentra en el diagrama, solo utiliza las clases de modelo para CONSULTAS


class Usuario():
    def buscarLibro(title):
        return Book.objects.filter(title__icontains=title)

class Estudiante(Student):
    def getPrestamo(loa_student):
        student_loa = Student.objects.get(loans=loa_student)
        return student_loa
    
    #Pendiente Revision
    def __init__(self,reg_est,first_est,last_est,e_mail_est):
     self.register = reg_est
     self.first_name = first_est
     self.last_name = last_est
     self.e_mail = e_mail_est

class Administrador(Admin):
    #Pendiente Revision
    def __init__(self,reg_adm,first_adm,last_adm,e_mail_adm):
     self.register = reg_adm
     self.first_name = first_adm
     self.last_name = last_adm
     self.e_mail = e_mail_adm

    def registrarEstudiante(nom_est,ape_est,e_ma_est,reg_est):
        est = Student.objects.create(first_name=nom_est,last_name=ape_est,e_mail=e_ma_est,register=reg_est)
        est.save()

    def actualizarEstudiante(reg_est,nom_est=None,ape_est=None,e_ma_est=None):
        
        est = Student.objects.get(register=reg_est)

        # Actualiza los valores si se proporcionan
        if nom_est is not None:
            est.first_name = nom_est
        if ape_est is not None:
            est.last_name = ape_est
        if e_ma_est is not None:
            est.e_mail = e_ma_est

        est.save()

    def eliminarEstudiante(reg_est):
        Student.objects.filter(register=reg_est).delete()

    def registrarLibro(reg_lib,ti_lib,aut_lib,cat_lib,edi_lib):
        lib = Book.objects.create(register=reg_lib,title=ti_lib,author=aut_lib,category=cat_lib,editorial=edi_lib)
        lib.save()

    def actualizarLibro(reg_lib,ti_lib=None,aut_lib=None):
        lib = Book.objects.get(register=reg_lib)

        if ti_lib is not None:
            lib.title = ti_lib
        if aut_lib is not None:
            lib.author = aut_lib

        lib.save()

    def eliminarLibro(reg_lib):
        Book.objects.filter(register=reg_lib).delete()
    
    def estadoPrestamoEstudiante(reg_student):
        loan_student = Student.objects.select_related("loans").get(register=reg_student)
    
    def agregarPrestamoEstudiante(reg_student,reg_book,date_loan,dev_date_loan):

        #creamos objeto Prestamo
        pres = Loan.objects.create(loan_date=date_loan,devolution_date=dev_date_loan,renew_tries=0,book=reg_book)
        pres.save()

        #Buscamos el estudiante
        estudiante = Student.objects.get(register=reg_student)

        #Asignamos el prestamo al estudiante
        #solo se puede usar .add() si en el modelo Student se ocupa ManyToManyField para el prestamo
        estudiante.loans.add(pres)
    
    def eliminarPrestamoEstudiante():
        Loan.objects.filter().delete

class Prestamo(Loan):

    def getLoan_date(date_loan):
        loan_date = Loan.objects.get(loan_date=loan_date)
        return loan_date
    
    def getDevolution_date(dev_loan):
        loan_dev = Loan.objects.get(devolution_date=dev_loan)
        return loan_dev
    
    def getBook(book_loan):
        loan_book = Loan.objects.get(book=book_loan)
        return loan_book
    
    #Pendiente
    def renovarPrestamo():
        return
    
class Libro(Book):
    #Pendiente Revision
    def __init__(self,reg_book,title_book,author_book,category_book,editorial_book):
        self.register = reg_book
        self.title = title_book
        self.author = author_book
        self.category = category_book
        self.editorial = editorial_book

    def getRegister(reg_book):
        book_reg = Book.objects.get(register=reg_book)
        return book_reg
    
    def getTitle(titl_book):
        book_titl= Book.objects.get(title=titl_book)
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