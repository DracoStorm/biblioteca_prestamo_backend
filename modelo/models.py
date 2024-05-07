from django.db import models
from .enums import Editorial, Category


# Acá solo van las TABLAS, por eso estan en ingles para diferenciarlas

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=[
        (c.value, c.name) for c in Category])
    editorial = models.CharField(max_length=50, choices=[
                                 (e.value, e.name) for e in Editorial])


class Loan(models.Model):
    loan_date = models.DateField(auto_now_add=True)
    devolution_date = models.DateField()
    renew_tries = models.IntegerField(
        default=0)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    e_mail = models.EmailField(max_length=60)

    class Meta:
        abstract = True


class StudentLoans(models.Model):
    loan_0 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_0', null=True)
    loan_1 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_1', null=True)
    loan_2 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_2', null=True)
    loan_3 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_3', null=True)
    loan_4 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_4', null=True)
    loan_5 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_5', null=True)
    loan_6 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_6', null=True)
    loan_7 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_7', null=True)
    loan_8 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_8', null=True)
    loan_9 = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_9', null=True)


class Student(User):
    register = models.IntegerField(primary_key=True)
    loans = models.ForeignKey(
        StudentLoans, on_delete=models.SET_NULL, null=True, default='NULL')


class Admin(User):
    register = models.IntegerField(primary_key=True)
