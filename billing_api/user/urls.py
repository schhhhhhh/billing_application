from django.urls import path

from user.views import ChangePasswordView, UpdateUserView, user_info


urlpatterns = [
    path('user/info/', user_info, name='user_info'),
    path('user/update-infos/', UpdateUserView.as_view(), name='user-update-infos'),
    # path('user/update-pwd/', ChangePasswordView.as_view(), name='user-update-pwd'),
    path('user/update-pwd/', ChangePasswordView.putPassword, name='user-update-pwd'),

]