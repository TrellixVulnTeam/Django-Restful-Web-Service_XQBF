from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.watchlist.urls')),
    path('api/account/', include('apps.accounts.urls')),
    path('api/', include('apps.watchlist.api.urls')),
]
