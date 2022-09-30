from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'myportfolio'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('github/', views.githubRepos, name='github_repos'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
    path('about/', views.about_me, name='about_me'),
]