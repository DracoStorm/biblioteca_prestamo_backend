from django.urls import path
from modelo import views

urlpatterns = [
    path('s/prestamo/', views.EstudiantePrestamo.as_view()),
    path('u/s_book/', views.BusquedaLibro.as_view())
]
