from django.contrib import admin
from django.urls import path, include
from .views import index  # импортируем представление

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),
    path('', index),  # добавляем маршрут для корневого URL
]