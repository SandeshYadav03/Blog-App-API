from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('blog-viewset', views.BlogViewSetAPI, basename="test")
router.register('blogs', views.BlogView)
router.register('comments', views.CommentView)

router.register('users', views.UserView)


urlpatterns = [
    # path('api-view', views.APIViews.as_view()),
    # path('api-view/<int:pk>/', views.APIViews.as_view()),
    path('', include(router.urls)), 
    path('login/',views.LoginView.as_view())
    
]