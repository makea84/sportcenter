from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^sportcenter/',include('userapp.urls'), namespace='userapp'),
    url(r'^sportcenter/pistas/',include('court.urls'), namespace='court'),
    url(r'^sportcenter/productos/',include('product.urls'), namespace='product'),
    url(r'^sportcenter/maquinas/',include('machine.urls'), namespace='machine'),
    url(r'^sportcenter/clases/',include('classroom.urls'), namespace='classroom'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^media/(?P<path>.*)$',{'document_root': settings.MEDIA_ROOT}),
    #url(r'^static/(?P<path>.*)$', {'document_root': settings.STATIC_ROOT})
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
