from django.urls import path, include
  
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]

# ---------- Router ----------
from rest_framework.routers import DefaultRouter
from .views import UserView, UserCreateView

router = DefaultRouter()
router.register('create', UserCreateView) # permissions.AllowAny
router.register('', UserView) # permissions.IsAdminUser

urlpatterns += router.urls