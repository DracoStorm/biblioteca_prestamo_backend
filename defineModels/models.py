from django.db import models
from .enums import Editorial, Category


# Acá solo van las TABLAS, por eso estan en ingles para diferenciarlas

class Book(models.Model):
    register = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=[
        (c.value, c.name) for c in Category])
    editorial = models.CharField(max_length=50, choices=[
                                 (e.value, e.name) for e in Editorial])


class Loan(models.Model):
    register = models.IntegerField(default=0,unique=True)
    loan_date = models.DateField(auto_now_add=True)
    devolution_date = models.DateField()
    renew_tries = models.IntegerField(
        default=0)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    e_mail = models.EmailField(default="", max_length=60)

    class Meta:
        abstract = True


class Student(User):
    register = models.IntegerField(unique=True)
    loans = models.ForeignKey(
        Loan, on_delete=models.SET_NULL, null=True, blank=True, default="")

class Admin(User):
    register = models.IntegerField(unique=True)