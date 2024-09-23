from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bookreview import urls as bookreview_urls
from users import urls as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(bookreview_urls)),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
