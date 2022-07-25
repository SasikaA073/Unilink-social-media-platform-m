from django.urls import path

from .views import SignUpView, UserDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/',
         UserDetailView.as_view(), name='user_detail'),
]