"""
URL configuration for fithome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coach.urls')),
    path('users/', include('users.urls')),

    path('reset-password/', auth_views.PasswordResetView.as_view(template_mame="users/reset_password.html"),
         name='reset_password'),
    path('reset-password_send/', auth_views.PasswordResetDoneView.as_view(template_mame="users/reset_password_send.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_mame="users/reset.html"),
         name='password_reset_confirm'),
    path('reset-password_complete/', auth_views.PasswordResetCompleteView.as_view(template_mame="users/reset_password_complete.html"),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

