
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('logintoken/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login URL for JWT
    path('token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),  # Token refresh URL
    path('protected/',views.protected_view, name='protected_view'),  # Protected view
    path('test-token',views.test_jwt_view),

]
