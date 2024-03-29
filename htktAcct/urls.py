"""
URL configuration for htktAcct project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path("", include("home.urls")),
    path("coa/", include("COA.urls")),
    path("companyinfo/", include("companyinfo.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path(
        "accounts/password_reset/",
        PasswordResetView.as_view(
            template_name="registration/password_reset_form.html"),
        name="password_reset",
    ),
    path(
        "accounts/login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "accounts/loggout/",
        LogoutView.as_view(template_name="registration/logged_out.html"),
        name="logout",
    ),
    path("admin/", admin.site.urls),
    path('customer/', include('customer.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
