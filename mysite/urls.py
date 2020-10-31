from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('capstone/', include('capstone.urls')),
    path('admin/', admin.site.urls),
]