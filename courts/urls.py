from django.urls import path, include
from . import views
urlpatterns = [
    path('courts', views.updateCourts, name="updatecourts"),
    path('courts/<int:pk>', views.removeCourts, name="removecourts"),
    path('viewcourt/<int:pk>', views.viewcourt, name = "viewcourt")
]
