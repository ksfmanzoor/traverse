from django.urls import path
from .views import ExperienceListView, CategoryDetailView, ExperienceDetailView, ExperienceCreateView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', ExperienceListView.as_view(), name='blog-home'),
    path('<int:pk>/', ExperienceDetailView.as_view(), name='post-detail'),
    path('category/<int:pk>/', CategoryDetailView)
    # path('', PostList.as_view(), name='blog-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('about/', views.about, name='blog-about'),

]


urlpatterns = format_suffix_patterns(urlpatterns)
