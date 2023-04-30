from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app.views import handler404, handler500

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('api/v1/users', UserViewSet.as_view({"get": "list"})),
    path('api/v1/categories/', AppCategoryViewSet.as_view({"get": "list"})),
    path('api/v1/apps/', AppViewSet.as_view({"get": "list"})),
    # path('api/v1/users/<int:id>/', UserViewSet.as_view({"get": "retrieve"})),
    path('api/v1/register/', RegisterViewAPI.as_view(), name='api_register'),
    path('api/v1/login/', UserLogin.as_view(), name='api_login'),
    path('api/v1/logout/', UserLogout.as_view(), name='api_logout'),
    # path('api/v1/auth/me/', AuthMe.as_view(), name='api_auth_user'),
    path('', Index.as_view(), name='home'),
    path('register', RegisterView.as_view(), name="register"),
    path('login', Login.as_view(), name="login"),
    path('logout', logout_form, name="logout"),
    path('apps/', include("app.urls")),

]

handler404 = handler404
handler500 = handler500

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
