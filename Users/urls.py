from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing, name = "landing"),
    path('login', views.loginuser, name = "login"),
    path('register/', views.register, name = "register"),
    path('logout/', views.logoutUser, name = "logout"),
    path('home/', views.home, name = "home"),
    path('denied', views.accessdenied , name = "accessdenied"),
    path('assignstaff', views.assignstaff, name = "assignstaff" ),
    path('revokestaff/<str:pk>', views.revokestaff, name = "revokestaff"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


