from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from users.views import CustomUserCreate

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]