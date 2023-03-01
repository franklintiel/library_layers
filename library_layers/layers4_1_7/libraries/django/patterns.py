from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from .functions import include, url


urlpatterns = [
    url('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
