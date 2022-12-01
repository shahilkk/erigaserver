
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls')),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

admin.site.site_header = "Eriga Administration"
admin.site.site_title = "Eriga  Admin Portal"
admin.site.index_title = "Welcome to Eriga Admin Portal"