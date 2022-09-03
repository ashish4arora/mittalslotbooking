from django.urls import path, include
from . import views
urlpatterns = [
    path('slots', views.updateSlots, name="updateslots"),
    path('slots/<int:pk>', views.removeSlots, name="removeslots"),
    path('calendar/<int:pk>', views.removeAssignment, name="removeassignment"),
]
