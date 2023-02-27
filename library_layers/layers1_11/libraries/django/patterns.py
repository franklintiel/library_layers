from .functions import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


