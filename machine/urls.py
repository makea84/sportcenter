from django.conf.urls import url

from . import views
 
urlpatterns = [
    url(r'^todas_maquinas/$', views.allMachines, name='todas_maquinas'),
    url(r'^maquina/$', views.get_machine, name='maquina'),
    url(r'^ejercicio/$', views.get_exercise, name='ejercicio'),
    url(r'^planificacion/$', views.get_planification, name='planificacion'),
    url(r'^programa/$', views.get_programm, name='programa'),
    url(r'^otros/$', views.get_other_user, name='otros'),
    url(r'^form_ejercicio/$', views.get_exercise_form, name='form_ejercicios'),
    url(r'^form_programa/$', views.get_programm_form, name='form_programa'),
    url(r'^form_planificacion/$', views.get_planification_form, name='form_planificacion'),
    url(r'^get_pdf/$',views.getPDF, name='get_pdf'),
    url(r'^prueba/$',views.example, name='prueba')
]