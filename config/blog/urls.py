from django.urls import path
from .views import HomeView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns =[
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('blog_details/<int:pk>', BlogDetailView.as_view(), name='blogdetails'),
    path('add_post/', BlogCreateView.as_view(), name='add_post'),
    path('update_post/edit/<int:pk>', BlogUpdateView.as_view(), name='update_post'),
    path('update_post/<int:pk>/delete', BlogDeleteView.as_view(), name='delete_post'),
]