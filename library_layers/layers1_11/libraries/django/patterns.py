from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .functions import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + staticfiles_urlpatterns()
