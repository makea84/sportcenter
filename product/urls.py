from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^todos_productos/$', views.allProducts),
    url(r'^producto/$', views.get_product),
    url(r'^stock/$', views.get_stock),
    url(r'^linea/$', views.get_line),
    url(r'^factura/$', views.get_bill),
    url(r'^otros/$', views.get_other_user),
    url(r'^form_stock/$', views.get_stock_form),
    url(r'^form_linea/$', views.get_line_form),
    url(r'^form_factura/$', views.get_bill_form),
]