from django.conf.urls import url

from . import views
appname='classroom'
urlpatterns = [
    url(r'^todas_clases/$', views.allClassrooms, name='todas_clases'),
    url(r'^clase/$', views.get_classroom, name='clase'),
    url(r'^curso/$', views.get_course, name='curso'),
    url(r'^mi_curso/$', views.get_my_course, name= 'mi_curso'),
    url(r'^no_curso/$', views.get_no_my_course, name='no_curso'),
    url(r'^participacion/$', views.get_participation, name='participacion'),
    url(r'^lugar/$', views.get_place, name='lugar'),
    url(r'^otros/$', views.get_other_user, name='otro'),
    url(r'^form_participacion/$', views.get_participation_form, name='form_participacion'),
    url(r'^form_lugar/$', views.get_place_form, name='form_lugar'),
]