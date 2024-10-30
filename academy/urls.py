from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from academy import settings
from main.views import get_user, courses_list_json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-user/', get_user, name='get-user'),
    path('api/course/', courses_list_json, name='courses_list_json'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



