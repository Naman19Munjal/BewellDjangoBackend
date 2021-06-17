from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('involve/', views.involve,name="story"),
    path('post/<str:slug>',views.postview,name="story"),
    path('volunteer/', views.volunteer,name="story"),
    path('donate/', views.donate,name="story"),
    path('games/', views.games,name="story"),
    path('games/findtheball', views.findtheball,name="story"),
    path('games/simon', views.simon,name="story"),
    path('games/match-the-slide', views.matchslide,name="story"),
    path('cures/', views.cures,name="story"),
    path('cures/breathing', views.breathing,name="story"),
    path('cures/meditation', views.meditation,name="story"),
    path('cures/story', views.story,name="story"),
    path('cures/song', views.song,name="story"),
    path('cures/yoga', views.yoga,name="story"),
    path('signup', views.sign_up, name="handleSignUp"),
    path('login', views.log_in, name="handleLogin"),
    path('logout', views.log_out, name="handleLogout"),
    path('doctor/', views.doctor, name="handleLogout"),

]