from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbe2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include('blog.urls')),
    url(r'^bombquiz/',include('bombquiz.urls')),
    url(r'^forum/',include('forum.urls')),
    url(r'^issues/',include('issues.urls')),
    
    #url(r'^media/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

