from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from app.views import handler404, handler500

from app.views import RegisterView, Index, Login, logout_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='home'),
    path('register', RegisterView.as_view(), name="register"),
    path('login', Login.as_view(), name="login"),
    path('logout', logout_form, name="logout"),
    path('apps/', include("app.urls")),

]

# handler404 = handler404
# handler500 = handler500

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



