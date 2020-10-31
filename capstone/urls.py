from django.urls import path

from . import views

app_name = 'capstone'
urlpatterns = [
    # ex: /capstone/typing example/results/
    path('<str:sentence>/results/', views.results, name='results'),
    # ex: /capstone/typing example/
    path('<str:sentence>/', views.detail, name='detail'),
]