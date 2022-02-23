from django.urls import path

from . import views

app_name='polls' #Por que colocar essa identificação? Não bastaria contar com a diferenciação do mysite/urls.py não?
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]