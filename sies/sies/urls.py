from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', 'empleados.views.signup', name='signup'),
    url(r'^signin/', 'empleados.views.signin', name='signin'),
)
