from .functions import include, url
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
]


