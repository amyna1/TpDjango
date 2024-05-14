# urls.py
from django.urls import path
from . import views


urlpatterns = [

    path('', views.PostList.as_view(), name='post-list'),  # Liste des publications
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),  # Détail d'une publication url lisible compresible
    path('post_create/', views.PostCreate.as_view(), name='post_create'),  # Création d'une nouvelle publication
    path('blog/post/<int:pk>/modifpost/', views.ModifyPost.as_view(), name='modifpost'),
    path('blog/<int:pk>/supprimer/', views.DeletePost.as_view(), name='supppost'),  # Suppression d'une publication
    path('logout', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),  
    path('register/', views.register, name='register'),
    path('ma_vue_protegee/', views.MaVueProtegee, name='ma_vue_protegee'),

]


