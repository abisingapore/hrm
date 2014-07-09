from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from webform.admin import HelloPDFView
from insurance.admin import HelloPDFViewInsurance
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'abiweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)), #admin interface
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^grappelli/', include('grappelli.urls')), #grappelli URLs
#   (r'^adminactions/', include('adminactions.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'webform.views.index', name="index"),
    url(r'^signup/', include('webform.urls')),
    url(r"^generate.pdf$", HelloPDFView.as_view()),
    url(r"^generate_insurance.pdf$", HelloPDFViewInsurance.as_view()),
)
