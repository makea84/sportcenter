from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^todas_pistas/$', views.allCourts),
    url(r'^pista/$', views.get_court),
    url(r'^reserva/$', views.get_reservation),
    url(r'^otros/$', views.get_other_user),
    url(r'^form_reserva/$', views.get_reservation_form),
] 