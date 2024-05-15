from django.urls import path
from modelo import views

urlpatterns = [
    path('u/sesion/', views.CtrlCrearSesion.as_view()),
    path('u/editorial/', views.CtrlBookEditorial.as_view()),
    path('u/category/', views.CtrlBookCategory.as_view()),
    path('e/loan/', views.CtrlEstudiantePrestamo.as_view()),
    path('e/book/', views.CtrlEstudianteLibro.as_view()),
    path('a/book/', views.CtrlAdminBook.as_view()),
    path('a/student/', views.CtrlAdminStudent.as_view()),
    path('a/student/loan/', views.CtrlAdminPrestamo.as_view())
]
