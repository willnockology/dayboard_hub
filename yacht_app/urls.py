from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # new line to define view for empty path
    path('dashboard/', views.dashboard, name='dashboard'),
    path('yacht/<int:yacht_id>/', views.yacht_detail, name='yacht_detail'),
    path('form/<int:form_id>/', views.form_detail, name='form_detail'),
    path('comment/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('notification/<int:notification_id>/', views.notification_detail, name='notification_detail'),
]
