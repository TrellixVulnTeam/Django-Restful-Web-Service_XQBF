from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('account/', include('accounts.urls', namespace='account')),
    path('movie/', include('movies.urls', namespace='movie')),
    path('api/movie/', include('movies.api.urls', namespace='movie-api')),
    path('api/watch/', include('movieplatform.urls', namespace='movie-platform')),
]
