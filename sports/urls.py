from django.urls import path, include
from . import views
urlpatterns = [
    path('sports', views.updateSports, name="updatesports"),
    path('delsport/<str:pk>', views.removeSports, name="removesports"),
    path('viewsport/<str:pk>', views.viewsport, name = 'viewsport')
]
