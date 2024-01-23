from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls.static import static

def static_urlpatterns():
    return static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static_urlpatterns()

# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
