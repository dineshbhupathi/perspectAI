from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from user.apis import userapi

api_router = DefaultRouter()
api_router.register('user', userapi.UserCreationApi, basename='user_creation')
api_router.register('employee', userapi.EmployeeCreation, basename='employee_creation')

urlpatterns = [
    url(r'^login/$', userapi.Login.as_view(), name='login'),
]
urlpatterns += api_router.urls
