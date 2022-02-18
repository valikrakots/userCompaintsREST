
from django.contrib import admin
from django.urls import include, path

from two.views import InfoAdminView, InfoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', include('users.urls')),
    path('api/tickets/', include('ticket.urls')),
    path('api/', InfoView.as_view(), name="info_user"),
    path('api/admin/', InfoAdminView.as_view(), name="info_admin"),
]
