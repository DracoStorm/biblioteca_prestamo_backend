from urllib.request import Request
from django.http import JsonResponse
from .modelo import Estudiante, Administrador
from .models import Student, Loan, StudentLoans, Book
from .serializers import StudentSerializer, LoanSerializer, StudentLoansSerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BusquedaLibro(APIView):
    def post(self, request):
        token = request.headers.get('token')
        try:
            usr = Estudiante(token) or Administrador(token)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        titulo = request.data.get('titulo')
        if titulo:
            try:
                b = usr.buscarLibro(titulo)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serial = BookSerializer(b, many=True)
            return JsonResponse(serial.data, safe=False)
        return Response(status=status.HTTP_404_NOT_FOUND)


class EstudiantePrestamo(APIView):
    def get(self, request):
        token = request.headers.get('token')
        try:
            estu = Estudiante(token)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        sl = estu.getPrestamos()
        serializer = StudentLoansSerializer(sl)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        token = request.headers.get('token')
        try:
            estu = Estudiante(token)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        pres = request.data.get('prestamo')
        if pres:
            try:
                p = estu.renovarPrestamo(pres)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serial = LoanSerializer(p)
            return JsonResponse(serial.data, safe=False)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AdminBook(APIView):
    def post(self, request):
        ...

    def patch(self, request):
        token = request.headers.get('token')
        try:
            admin = Administrador(token)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        id = request.headers.get('id')
        if id:
            b = admin.actualizarLibro(id, request.headers.get(
                'titulo'), request.headers.get('autor'))
            serial = BookSerializer(b)
            return Request(serial.data, status=status.HTTP_200_OK)
        return Request(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        token = request.headers.get('token')
        try:
            admin = Administrador(token)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            l = admin.registrarLibro(request.headers.get('titulo'),
                                     request.headers.get('autor'),
                                     request.headers.get('editorial'),
                                     request.headers.get('categoria'))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serial = BookSerializer(l)
        return Response(serial.data, status=status.HTTP_201_CREATED)
