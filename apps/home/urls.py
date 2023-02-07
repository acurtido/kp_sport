from django.urls import path, re_path, include
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('crear-actividad', views.crear_actividad, name='crear-actividad'),
    path('actualizar-actividad/<str:pk>/', views.actualizar_actividad, name='actualizar-actividad'),
    path('eliminar-actividad/<str:pk>/', views.eliminar_actividad, name='eliminar-actividad'),
    path('actividades', views.listar_actividades, name='actividades'),
    path('actividad/<str:pk>/', views.ver_actividad, name='actividad'),
    path('crear-encuentro', views.crear_encuentro, name='crear-encuentro'),
    path('actualizar-encuentro/<str:pk>/', views.actualizar_encuentro, name='actualizar-encuentro'),
    re_path(r'^emoji/', include('emoji.urls')),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
