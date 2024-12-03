from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('', include('quizes.urls')),
    path('', include('questions.urls')),
    path('results/', include('results.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_title = "Geografiya-Admin"
admin.site.site_header = "Admin"
admin.site.index_title = "Geografiya-Admin"