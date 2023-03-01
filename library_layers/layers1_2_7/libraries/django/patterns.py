from django.contrib import admin

from .functions import patterns, include, url


urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls))
)
