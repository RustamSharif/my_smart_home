from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateView, SensorDetailView, MeasurementCreateView, MeasurementListView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor-retrieve-update'),
    path('sensors/detail/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
    path('measurements/list/', MeasurementListView.as_view(), name='measurement-list')  # Добавлен маршрут для списка измерений
]