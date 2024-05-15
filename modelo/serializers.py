from pkg_resources import require
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
    loan_0 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)
    loan_1 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)
    loan_2 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)
    loan_3 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)
    loan_4 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)
    loan_5 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)
    loan_6 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)
    loan_7 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)
    loan_8 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)
    loan_9 = serializers.PrimaryKeyRelatedField(
        queryset=Loan.objects.all(), required=False, allow_null=True)

    class Meta:
        model = StudentLoans

    def to_representation(self, instance):
        loans = []
        for i in range(10):
            loan_field_name = f'loan_{i}'
            loan_instance = getattr(instance, loan_field_name)
            if loan_instance:
                loans.append(LoanSerializer(loan_instance).data)
        # Return a dict with the list
        return {'loans': loans}


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['register', 'first_name', 'last_name', 'e_mail']
