from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar
from django.conf.urls.static import static
from bookreview import urls as bookreview_urls
from users import urls as users_urls

urlpatterns = [

    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('users/', include('users.urls')),
    path('', include(bookreview_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

