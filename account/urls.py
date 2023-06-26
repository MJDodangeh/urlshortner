from django.urls import path
from .views import RegisterApi
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]