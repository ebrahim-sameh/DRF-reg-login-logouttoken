from rest_framework import routers, viewsets
from userapi import views
from django.urls import path,include
from userapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register',views.UserProfileViewSet)


urlpatterns = [

    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls))
    
]
