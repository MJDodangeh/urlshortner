from django.urls import path
from .views import makeUrl,redirectUrl,viewCount
urlpatterns = [
    path('shorten/', makeUrl.as_view()),
    path('<str:shorturl>', redirectUrl.as_view()),
    path('viewcount/', viewCount.as_view())
]