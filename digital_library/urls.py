
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('webpages.urls')),
    path('accounts/', include('accounts.urls')),
    path('book/', include('books.urls')),
    path('category/', include('category.urls')),
    path('enrollment/', include('enrollment.urls')),
    path('payment/', include('payment.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
