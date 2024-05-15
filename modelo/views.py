from .modelo import Estudiante, Administrador
from .models import Admin, Category, Student, Loan, StudentLoans, Book, Editorial
from .serializers import CategorySerializer, StudentSerializer, LoanSerializer, StudentLoansSerializer, BookSerializer, EditorialSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CtrlSesion():
    def crearSesion(self, id: int, nombre: str, apellido: str):
        if id > 999999999 or id <= 99999999:
            return None
        if id <= 199000000:
            try:
                a = Admin.objects.get(
                    register=id, first_name=nombre, last_name=apellido)
            except Admin.DoesNotExist:
                return None
            else:
                return a.token
        else:
            try:
                s = Student.objects.get(
                    register=id, first_name=nombre, last_name=apellido)
            except Student.DoesNotExist:
                return None
            else:
                return s.token

    def validarSesion(self, request, permision: str):
        token = request.headers.get('token')
        if token:
            if permision == 'administrador':
                try:
                    a = Administrador(token)
                except:
                    return None
                else:
                    return a
            if permision == 'estudiante':
                try:
                    e = Estudiante(token)
                except:
                    return None
                else:
                    return e
        return None


class Sesion(APIView):
    def post(self, request):
        id = request.headers.get('id')
        nombre = request.headers.get('first-name')
        apellido = request.headers.get('last-name')
        if id and nombre and apellido:
            token = CtrlSesion().crearSesion(int(id), nombre, apellido)
            if token:
                return Response(headers={'token': token})
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class EstudianteLibro(APIView):
    def post(self, request):
        admin = CtrlSesion().validarSesion(request, permision='estudiante')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            s = admin.buscarLibro(request.data.get('title'),
                                  request.data.get('author'),
                                  request.data.get('editorial'),
                                  request.data.get('category'))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not s:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serial = BookSerializer(s, many=True)
        return Response(serial.data)


class EstudiantePrestamo(APIView):
    def get(self, request):
        estu = CtrlSesion().validarSesion(request, permision='estudiante')
        if not estu:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        sl = estu.getPrestamos()
        serializer = StudentLoansSerializer(sl)
        return Response(serializer.data)

    def post(self, request):
        estu = CtrlSesion().validarSesion(request, permision='estudiante')
        if not estu:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # print(request.data)
        pres: int = request.data.get('id_loan')
        if pres:
            try:
                p = estu.renovarPrestamo(pres)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serial = LoanSerializer(p)
            return Response(serial.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AdminBook(APIView):
    def post(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            s = admin.buscarLibro(request.data.get('title'),
                                  request.data.get('author'),
                                  request.data.get('editorial'),
                                  request.data.get('category'))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not s:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serial = BookSerializer(s, many=True)
        return Response(serial.data)

    def patch(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        id = request.data.get('id')
        if id:
            try:
                b = admin.actualizarLibro(id,
                                          request.data.get('title'),
                                          request.data.get('author'),
                                          request.data.get('editorial'),
                                          request.data.get('category'))
            except:
                return Response(status=status.HTTP_304_NOT_MODIFIED)
            serial = BookSerializer(b)
            return Response(serial.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            l = admin.registrarLibro(request.data.get('title'),
                                     request.data.get('author'),
                                     request.data.get('editorial'),
                                     request.data.get('category'))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serial = BookSerializer(l)
        return Response(serial.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        id = request.data.get('id')
        if id:
            try:
                admin.eliminarLibro(id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AdminStudent(APIView):
    def post(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            s = admin.buscarEstudiante(request.data.get('register'),
                                       request.data.get('first_name'),
                                       request.data.get('last_name'),
                                       request.data.get('e_mail'))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not s:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serial = StudentSerializer(s, many=True)
        return Response(serial.data)

    def patch(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        register = request.data.get('register')
        if register:
            try:
                s = admin.actualizarEstudiante(register,
                                               request.data.get('first_name'),
                                               request.data.get('last_name'),
                                               request.data.get('e_mail'))
            except:
                return Response(status=status.HTTP_304_NOT_MODIFIED)
            serial = StudentSerializer(s)
            return Response(serial.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            s = admin.registrarEstudiante(request.data.get('register'),
                                          request.data.get('first_name'),
                                          request.data.get('last_name'),
                                          request.data.get('e_mail'))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serial = StudentSerializer(s)
        return Response(serial.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        id = request.data.get('register')
        if id:
            try:
                admin.eliminarEstudiante(id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AdminPrestamo(APIView):
    def post(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        register = request.data.get('register')
        if register:
            try:
                sl = admin.estadoPrestamoEstudiante(register)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                serial = StudentLoansSerializer(sl)
                return Response(serial.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            sl = admin.agregarPrestamoEstudiante(
                request.data.get('register'),
                request.data.get('id_book'))
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serial = StudentLoansSerializer(sl)
            return Response(serial.data)

    def delete(self, request):
        admin = CtrlSesion().validarSesion(request, permision='administrador')
        if not admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            admin.eliminarPrestamoEstudiante(
                request.data.get('register'),
                request.data.get('id_loan'))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class BookCategory(APIView):
    def get(self, request):
        serial = CategorySerializer(Category.objects.all(), many=True)
        return Response(serial.data)


class BookEditorial(APIView):
    def get(self, request):
        serial = EditorialSerializer(Editorial.objects.all(), many=True)
        return Response(serial.data)
