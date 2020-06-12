from django.contrib import admin
from django.urls import path
import post.views   # post에 있는 views.py를 가져와라
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post.views.home, name='home'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)