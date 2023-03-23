from django.urls import path
from .views import PostList, PostDetail, PostNewsCreate, PostUpdate, PostArticlesCreate, PostDelete

urlpatterns = [

    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', PostNewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='product_delete'),
    path('articles/create/', PostArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
]
