from django.conf.urls import url

from . import views
appname='court'
urlpatterns = [
    url(r'^todas_pistas/$', views.allCourts, name='todas_pistas'),
    url(r'^pista/$', views.get_court, name='pistas'),
    url(r'^reserva/$', views.get_reservation,name='reserva'),
    url(r'^otros/$', views.get_other_user, name='otros'),
    url(r'^form_reserva/$', views.get_reservation_form, name='form_reserva'),
] 