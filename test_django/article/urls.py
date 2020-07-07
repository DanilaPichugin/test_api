from django.urls import path
from .views import ArticleViewSet #ArticleView #SingleArticleView
from rest_framework.routers import DefaultRouter

#app_name = "articles"
# app_name will help us do a reverse look-up latter.

#urlpatterns = [
#    path('articles/', ArticleView.as_view()),
    #path('articles/<int:pk>', ArticleView.as_view()),
#    path('articles/<int:pk>', SingleArticleView.as_view()),
#]
router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')

urlpatterns = router.urls
