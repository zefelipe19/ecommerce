from django.urls import path

from . import views


urlpatterns = [
    path('items/', views.ItemView.as_view(), name='items')
]
