from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('acounts.urls')), #ira chamar nosso url acounts para mostrar o cadastro etc
    path('', views.redirecionando), #ira redirecionar para o url accounts/cadastro
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
