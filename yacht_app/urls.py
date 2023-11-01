from django.urls import path
from . import views
from .views import UserLoginView
from .views import UserLogoutView

urlpatterns = [
    path('', views.index, name='index'),  # new line to define view for empty path
    path('dashboard/', views.dashboard, name='dashboard'),
    path('yacht/<int:yacht_id>/', views.yacht_detail, name='yacht_detail'),
    path('form/<int:form_id>/', views.form_detail, name='form_detail'),
    path('comment/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('notification/<int:notification_id>/', views.notification_detail, name='notification_detail'),
    path('register/', views.register, name='register'),
    path('your_login_view/', views.your_login_view, name='your_login_view'),
    path('home/', views.home, name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),




]
