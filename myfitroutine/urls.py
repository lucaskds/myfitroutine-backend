"""myfitroutine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from apps.user.views import RegisterView

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version="1.0.0",
        description="API documentation of App",
    ),
    public=True,
)

urlpatterns = [
    re_path(r"^api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    re_path(r"^api/auth/token/obtain/$", TokenObtainPairView.as_view()),
    re_path(r"^api/auth/token/refresh/$", TokenRefreshView.as_view()),
    re_path(r"^api/register/", RegisterView.as_view(), name="auth_register"),
]

urlpatterns += [
    re_path(r"^admin/", admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
]
urlpatterns += [
    re_path(r"^api/users/", include("apps.user.urls")),
]
urlpatterns += [
    re_path(r"^api/training/", include("apps.train.urls")),
]
urlpatterns += [
    re_path(r"^api/nutrition/", include("apps.nutrition.urls")),
]

urlpatterns += [
    re_path(
        "swagger-ui/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-schema",
    ),
]
