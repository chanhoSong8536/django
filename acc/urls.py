from django.urls import path
from. import views
app_name =  "acc"
urlpatterns = [
    path('index/',views.index, name="index"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('signup/', views.signup, name="signup"),
    path('update/', views.update, name="update"),
    path('delete/', views.delete, name="delete")
]