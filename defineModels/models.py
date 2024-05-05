from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class Libro(models.Model):
    opciones_categoria = [
        ('Educativo','Ciencia Ficcion','Romance','Misterio')
    ]
    opciones_editorial = [
        ('Porrua','Alfa Omega','Fondo de Bikini','Crustaseo Cascarudo')
    ]

    matricula = models.IntegerField(unique=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50,choices=opciones_categoria)
    editorial = models.CharField(max_length=50, choices=opciones_editorial)

    def getMatricula(self):
        return self.matricula
    
    def getTitulo(self):
        return self.titulo
    
    def getAutor(self):
        return self.autor
    
    def getCategoria(self):
        return self.categoria
    
    def getEditorial(self):
        return self.editorial
    
    def setTitulo(self,t):
        self.titulo = t
    
    def setAutor(self,a):
        self.autor = a

    def setCategoria(self,c):
        self.categoria = c

    def setEditorial(self,ed):
        self.editorial = ed
        

class Prestamo(models.Model):
    #matricula = models.IntegerField(unique=True)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField()
    vecesRenovado = models.IntegerField(default=0,validators=[MaxValueValidator(2)])
    libro= models.ForeignKey(Libro,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    def getFechaPrestamo(self):
        return str(self.fecha_prestamo)
    
    def getFechaDevolucion(self):
        return str(self.fecha_devolucion)
    
    def getLibro(self):
        return self.libro
    
    def renovarPrestamo(self):
        if self.vecesRenovado >= 0 or self.vecesRenovado <= 2:
            self.vecesRenovado += 1
            self.save()
            return True
        else:
            return False

class Usario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correoElectronico = models.EmailField(default="",max_length=60)

    class Meta:
        abstract=True
    
    def busquedaLibros(self):
        return 
    
class Estudiante(Usario):
    matricula = models.IntegerField(unique=True)
    prestamo = models.ForeignKey(Prestamo,on_delete=models.SET_NULL,null=True,blank=True,default="")

    def getPrestamo(self):
        return self.prestamo
    
class Administrador(Usario):
    matricula = models.IntegerField(unique=True)

    def registrarEstudiante():
        return
    def actualizarEstudiante():
        return
    def eliminarEstudiante():
        return
    def registrarLibro():
        return
    def actualizarLibro():
        return
    def eliminarLibro():
        return
    def estadoPrestamoEstudiante():
        return
    def agregarPrestamoEstudiante():
        return
    def eliminarPrestamoEstudiante():
        return

    
    
    
