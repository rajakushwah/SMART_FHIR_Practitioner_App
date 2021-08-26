from . import views
from django.urls import path,include

urlpatterns = [
    path('result',views.result,name='result'),
    path('',views.index,name='index' ),
    path('about',views.about,name='about' ),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('info', views.info, name="info"),
    path('patient', views.patient, name="patient"),
    path('observation', views.observation, name="observation"),
    path('practitioner', views.practitioner, name="practitioner"),
    path('medication', views.medication, name="medication"),

]