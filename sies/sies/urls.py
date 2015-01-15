from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from eventos.views import EventoViewSet

router = routers.DefaultRouter()
router.register(r'eventos', EventoViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', 'empleados.views.signup', name='signup'),
    url(r'^signin/$', 'empleados.views.signin', name='signin'),
    url(r'^registro/', 'userprofiles.views.register', name='register'),
    url(r'^logout/$', 'empleados.views.user_logout', name='logout'),
    url(r'^socios/', 'empleados.views.socios', name='socios'),
    url(r'^eventos/(?P<teatro>[\w\-\W]+)', 'eventos.views.eventos', name='empleados'),
    url(r'^evento/$', 'eventos.views.event_list', name='lista_eventos'),
    url(r'^profile/$', 'userprofiles.views.userprofile', name='userprofiles'),
    url(r'^lista/$', 'listas_asistencias.views.lista', name='lista'),
    url(r'^login/$', 'userprofiles.views.login', name='login'),
    url(r'^cancelar/$', 'empleados.views.cancelar', name='cancelar'),
    url(r'^api/', include(router.urls)),

 
)
