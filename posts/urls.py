from . import views
from django.urls import path


urlpatterns=[
    path('homepage/',views.homepage,name="posts_home"),
    path('',views.PostListCreateView.as_view(),name="list_posts"),
    path('<int:post_id>/',views.PostRetrieveUpdateDeleteView.as_view(),name="retrieve_update_delete_posts"),
]

