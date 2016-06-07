from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^todas_clases/$', views.allClassrooms),
    url(r'^clase/$', views.get_classroom),
    url(r'^curso/$', views.get_course),
    url(r'^mi_curso/$', views.get_my_course),
    url(r'^no_curso/$', views.get_no_my_course),
    url(r'^participacion/$', views.get_participation),
    url(r'^lugar/$', views.get_place),
    url(r'^otros/$', views.get_other_user),
    url(r'^form_participacion/$', views.get_participation_form),
    url(r'^form_lugar/$', views.get_place_form),
]