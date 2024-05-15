from django.urls import path
from modelo import views

urlpatterns = [
    path('u/sesion/', views.Sesion.as_view()),
    path('u/editorial/', views.BookEditorial.as_view()),
    path('u/category/', views.BookCategory.as_view()),
    path('e/loan/', views.EstudiantePrestamo.as_view()),
    path('e/book/', views.EstudianteLibro.as_view()),
    path('a/book/', views.AdminBook.as_view()),
    path('a/student/', views.AdminStudent.as_view()),
    path('a/student/loan/', views.AdminPrestamo.as_view())
]
