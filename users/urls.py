from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("register_user/", views.register_user, name="register_user"),
    path("change_password/", views.change_password, name="change_password"),

    path('reset-password/', views.custom_password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>/', views.custom_password_reset_confirm, name='custom_password_reset_confirm'),
]  

# urlpatterns = [
#     path("register_user/", views.register_user, name="register_user"),

#     # # 🔐 Login / Logout
#     # path("login/", auth_views.LoginView.as_view(), name="login_user"),
#     # path("logout/", auth_views.LogoutView.as_view(), name="logout_user"),

#     # 🔁 Password Change (when user is logged in)
#     path("password_change/", auth_views.PasswordChangeView.as_view(), name="change_password"),
#     path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

#     # 🔄 Password Reset (when user forgets password)
#     path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
#     path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
#     path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
#     path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
# ]
