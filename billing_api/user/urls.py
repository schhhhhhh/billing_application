from django.urls import path

from user.views import user_info


urlpatterns = [
    path('user_info/', user_info, name='user_info'),
]