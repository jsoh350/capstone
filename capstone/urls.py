from django.urls import path

from . import views

app_name = 'capstone'
urlpatterns = [
    # ex: /capstone/typing example/results/
    path('<str:sentence>/results/', views.results, name='results'),
    # ex: /capstone/typing example/
    path('<str:sentence>/', views.complete, name='complete'),
    # ex: /capstone/getLB/<email&type>
    path('<int:input_type>', views.leaderboard, name='leaderboard'),
]
