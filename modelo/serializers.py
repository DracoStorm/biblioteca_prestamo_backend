from rest_framework import serializers
from .models import Category, Editorial, Student, Loan, Book, StudentLoans


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    editorial = EditorialSerializer()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'editorial']


class LoanSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Loan
        fields = ['id', 'loan_date', 'devolution_date', 'renew_tries', 'book']


class StudentLoansSerializer(serializers.ModelSerializer):
    loan_0 = LoanSerializer()
    loan_1 = LoanSerializer()
    loan_2 = LoanSerializer()
    loan_3 = LoanSerializer()
    loan_4 = LoanSerializer()
    loan_5 = LoanSerializer()
    loan_6 = LoanSerializer()
    loan_7 = LoanSerializer()
    loan_8 = LoanSerializer()
    loan_9 = LoanSerializer()

    class Meta:
        model = StudentLoans
        fields = ['id', 'loan_0', 'loan_1', 'loan_2', 'loan_3',
                  'loan_4', 'loan_5', 'loan_6', 'loan_7', 'loan_8', 'loan_9']

    def to_representation(self, instance):
        # Call the superclass's to_representation method
        data = super().to_representation(instance)

        # Filter out fields with null values
        return {key: value for key, value in data.items() if value}


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['register', 'first_name', 'last_name', 'e_mail', 'loans_id']
