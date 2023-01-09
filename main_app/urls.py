from django.urls import path
from . import views
urlpatterns = [
    path('fighter.html', views.fighter),
    path('index.html', views.index),
    path('', views.index),
    path('blog.html', views.blog),
    path('single-blog.html', views.sb),
    path('team.html', views.teams),
    path('tajrib.html', views.tajrib),
    path('contact.html', views.contact),
    path('Twenties.html',views.Twenties),
    path('Tens.html',views.Tens),
    path("Noresult.html", views.search),
    path("Nothing.html", views.search),
    path("U10.html", views.u10),
    path('<int:id>/', views.GG, name='GG'),
    path('signup', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('s', views.search)
]