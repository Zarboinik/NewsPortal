from django.urls import path
from django.views.decorators.cache import cache_page

from .views import PostList, PostDetail, PostNewsCreate, PostUpdate, PostArticlesCreate, PostDelete, CategoryListView, \
    subscribe, subscriptions

urlpatterns = [

    path('', cache_page(60)(PostList.as_view()), name='post_list'),
    path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
    path('news/create/', PostNewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/create/', PostArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('subscriptions/<int:pk>', subscribe, name='subscribe'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
