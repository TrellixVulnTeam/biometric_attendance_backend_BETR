from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('attendanceSystem.api.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]
