from django.urls import path

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, switch_published

app_name = 'blog'
urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('is_published/<int:pk>/', switch_published, name='switch_published')
]
