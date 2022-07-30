from django.contrib import admin
from django.urls import path, include

app_name = 'landing'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls'))
]
