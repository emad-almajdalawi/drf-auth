from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import MemesListCreateAPI, MemesDetailUpdateDeleteAPI


urlpatterns = [
    path('api/memes-list', MemesListCreateAPI.as_view(), name='memes-list'),
    path('api/<int:pk>', MemesDetailUpdateDeleteAPI.as_view(), name='memes-detail'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/memes-no-img', MemesListCreateAPI.as_view(), name='memes-no-img'),
]

