from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^todos_productos/$', views.allProducts, name='todos_productos'),
    url(r'^producto/$', views.get_product, name='producto'),
    url(r'^stock/$', views.get_stock, name='stock'),
    url(r'^linea/$', views.get_line, name='linea'),
    url(r'^factura/$', views.get_bill, name='factura'),
    url(r'^otros/$', views.get_other_user, name='otros'),
    url(r'^form_stock/$', views.get_stock_form, name='form_stock'),
    url(r'^form_linea/$', views.get_line_form, name='form_linea'),
    url(r'^form_factura/$', views.get_bill_form, name='form_factura'),
]