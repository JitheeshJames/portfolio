from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_feedback',views.user_feedback, name='user_feedback'),
    path('proj_display/<int:id>',views.proj_display, name = 'proj_display'),
]