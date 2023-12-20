"""
URL configuration for billing_api project.

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
from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from billing_api import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Billing API Documentation",
      default_version='v1',
      description="API REST pour une mini application de facturation",
      terms_of_service="https://client-billing.vercel.app",
      contact=openapi.Contact(email="schzao@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('customer_app.urls')),
    path('api/', include('category_app.urls')),
    path('api/', include('product_app.urls')),
    path('api/', include('invoice_app.urls')),
    path('api/', include('user.urls')),

    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)