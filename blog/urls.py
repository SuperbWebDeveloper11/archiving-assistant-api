from django.urls import include, path
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import views_for_api as apiviews
from .views import views_for_html_rendering as html_rendering_views
from .views import views_for_comments as comment_views

app_name = 'blog'

urlpatterns = [
    ####################### urls for API #######################
    # posts urls
    path('api/', apiviews.PostList.as_view()),
    path('api/<int:pk>/', apiviews.PostDetail.as_view()),
    # comments urls
    path('api/<int:pk>/comments/', apiviews.CommentList.as_view()),
    path('api/<int:pk>/comments/<int:comment_pk>/', apiviews.CommentDetail.as_view()),
    # postlikes urls
    path('api/<int:pk>/postlikes/', apiviews.PostlikeList.as_view()),
    path('api/<int:pk>/postlikes/<int:postlike_pk>/', apiviews.PostlikeDetail.as_view()),

    ####################### urls for Django Template rendering #######################
    # posts urls 
    path('', html_rendering_views.PostList.as_view(), name='post_list'),
    path('add/', html_rendering_views.PostCreate.as_view(), name='post_add'),
    path('<int:pk>/detail/', html_rendering_views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/update/', html_rendering_views.PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', html_rendering_views.PostDelete.as_view(), name='post_delete'),

    ####################### urls for creating comments with jQuery #######################
    # comments urls 
    path('<int:pk>/comments/', comment_views.CommentList.as_view(), name='comment_list'),
    path('<int:pk>/comments/add/', comment_views.CommentCreate.as_view(), name='comment_create'),
    path('<int:pk>/comments/<int:comment_pk>/update/', comment_views.CommentUpdate.as_view(), name='comment_update'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', comment_views.CommentDelete.as_view(), name='comment_delete'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

