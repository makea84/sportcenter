from django.conf.urls import url

from . import views
 
urlpatterns = [
    url(r'^todas_maquinas/$', views.allMachines),
    url(r'^maquina/$', views.get_machine),
    url(r'^ejercicio/$', views.get_exercise),
    url(r'^planificacion/$', views.get_planification),
    url(r'^programa/$', views.get_programm),
    url(r'^otros/$', views.get_other_user),
    url(r'^form_ejercicio/$', views.get_exercise_form),
    url(r'^form_programa/$', views.get_programm_form),
    url(r'^form_planificacion/$', views.get_planification_form),
    url(r'^get_pdf/$',views.getPDF),
    url(r'^prueba/$',views.example)
]