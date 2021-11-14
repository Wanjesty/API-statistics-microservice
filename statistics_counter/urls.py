from django.urls import path
from . import views


urlpatterns = [
    path('show/', views.ShowStatisticView.as_view()),
    path('add/',views.AddStatisticView.as_view()),
    path('delete/', views.DeleteStatisticView.as_view())
]