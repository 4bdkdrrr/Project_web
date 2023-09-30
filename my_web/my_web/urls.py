from django.conf import settings
from posting.views import index
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from posting import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
