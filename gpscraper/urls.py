from django.urls import path
from . import views
from gpscraper.views import HomeView, AppSearchView, AppDetailView, Results, AboutView, Landing

app_name = "gpscraper"


urlpatterns = [
    path('', views.Landing, name='Landing'),


    path('home', views.HomeView, name='home'),

    path('about', views.AboutView, name='about'),

    path('app/search/', AppSearchView.as_view(), name='app_search'),

    path('app/results/', views.Results, name='results'),

    path('app/detail/<uid>/', AppDetailView.as_view(), name='app_detail'),

]

