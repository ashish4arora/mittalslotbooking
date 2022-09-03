from django.urls import path, include
from . import views
urlpatterns = [
    path('inventory', views.updateInventory, name="updateinventory"),
    path('inventory/<int:pk>', views.removeInventory, name="removeinventory"),
    path('item/<int:pk>', views.removeItem, name="removeitem")
]
