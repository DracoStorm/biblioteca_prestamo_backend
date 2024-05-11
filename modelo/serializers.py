from rest_framework import serializers
from .models import Student, Loan, Book, StudentLoans


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'editorial']


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'loan_date', 'devolution_date', 'renew_tries', 'book']


class StudentLoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLoans
        fields = ['id', 'loan_0', 'loan_1', 'loan_2', 'loan_3',
                  'loan_4', 'loan_5', 'loan_6', 'loan_7', 'loan_8', 'loan_9']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['register', 'first_name', 'last_name', 'e_mail', 'loans_id']
