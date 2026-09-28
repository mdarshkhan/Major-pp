from django.urls import path
from . import views

urlpatterns = [
    path('userhome/', views.userhome, name='userhome'),
    path('userpredict/', views.userpredict, name='userpredict'),
    path('userregister/', views.userregister, name='userregister'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('userdata/', views.userdata, name='userdata'),  # ✅ NEW
]

