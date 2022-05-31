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


# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDAzNTE1MCwiaWF0IjoxNjUzOTQ4NzUwLCJqdGkiOiJmMjZjOTJiZTIxMGM0Mzg4YjM2ZmIzMjMzYjFhZmZlNSIsInVzZXJfaWQiOjF9.kTkSp-6rNNJWL1mo_44pDPly4b_hfpsNBYtyPfc3cUQ",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzOTQ5MDUwLCJpYXQiOjE2NTM5NDg3NTAsImp0aSI6ImU0NGMzNzY2OTYzZDRlMTI4NmIzZWFkODg4YjJiNTRlIiwidXNlcl9pZCI6MX0.reARpX9oIJaYhbqi8gc1o0e49aSEMulwsgmtemCociI"
# }