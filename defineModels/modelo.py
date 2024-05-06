from typing import Any
from .models import Student, User,Admin,Loan,Book
from django.utils import timezone
from datetime import timedelta

# Acá va el MODELO, el que se encuentra en el diagrama, solo utiliza las clases de modelo para CONSULTAS


class Usuario():
    def buscarLibro(title):
        return Book.objects.filter(title__icontains=title)

class Estudiante(Student):
    def getPrestamo():
        return 
    
    #Por corregir
    def __init__(self,reg_est,first_est,last_est,e_mail_est):
     self.register = reg_est
     self.first_name = first_est
     self.last_name = last_est
     self.e_mail = e_mail_est

class Administrador(Admin):
    
    # def __init__(self,reg_adm,first_adm,last_adm,e_mail_adm):
    #  self.register = reg_adm
    #  self.first_name = first_adm
    #  self.last_name = last_adm
    #  self.e_mail = e_mail_adm

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
        lib.save

    def actualizarLibro(reg_lib,ti_lib=None,aut_lib=None):
        lib = Book.objects.get(register=reg_lib)

        if ti_lib is not None:
            lib.title = ti_lib
        if aut_lib is not None:
            lib.author = aut_lib

        lib.save()

    def eliminarLibro(reg_lib):
        Book.objects.filter(register=reg_lib).delete()
    
    #corregir Pendiente
    def estadoPrestamoEstudiante(reg_loan):
       est_lib = Loan.objects.get(register=reg_loan)
       return est_lib

    def agregarPrestamoEstudiante(loan_lib=timezone.now(),book_lib=None):
        pres = Loan.objects.create(loan_date=loan_lib,book=book_lib)
        pres.save()
    #corregir Pendiente

    def eliminarPrestamoEstudiante():
        Loan.objects.filter().delete

class Prestamo(Loan):

    def getLoan_date():
        return Loan.loan_date
    def getDevolution_date():
        return Loan.devolution_date
    def getBook():
        return Loan.book
    def renovarPrestamo():
        return
    
class Libro(Book):
    #Por corregir
    def __init__(self,reg_book,title_book,author_book,category_book,editorial_book):
        self.register = reg_book
        self.title = title_book
        self.author = author_book
        self.category = category_book
        self.editorial = editorial_book

    def getRegister():
        return Book.register
    def getTitle():
        return Book.title
    def getAthor():
        return Book.author
    def getCategory():
        return Book.category
    def getEditorial():
        return Book.editorial
    
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