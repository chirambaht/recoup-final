from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about', views.about, name="about"),
    path('login', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('login/practice', auth_views.LoginView.as_view(template_name='dashboard/practice-login.html'), name='loginPractice'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
    path('register', views.register, name="register"),
    path('register/practice', views.register, name="registerPractice"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)