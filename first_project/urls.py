
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


import basic_app
app_name=basic_app

urlpatterns = [
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('basic_app.urls')))

prefix_default_language=False


urlpatterns +=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)