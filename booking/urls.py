from django.urls import path, include
from . import views
urlpatterns = [
    path('bookings', views.updateBooking, name="updatebooking"),
    path('booking/<int:pk>', views.removeBooking, name="removebooking")
]
