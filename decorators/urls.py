from django.urls import path

from . import views

urlpatterns = [
    path('enter-name-with-decorator/', views.enter_name_with_decorator,
         name='Enter Name With Decorator'),
    path('enter-name-no-decorator/', views.enter_name_no_decorator,
         name='Enter Name No Decorator'),
]
