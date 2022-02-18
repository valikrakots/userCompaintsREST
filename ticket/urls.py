from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from ticket import views
from ticket.views import (DiscussionAdminView, DiscussionView,
                          TicketAdminClosedView, TicketAdminDetailView,
                          TicketAdminFrozenView, TicketAdminPendingView,
                          TicketAdminView, TicketClosedView, TicketDetailView,
                          TicketFrozenView, TicketList, TicketPendingView)

urlpatterns = [
    path('', TicketList.as_view(), name='ticketslist'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticketdetail'),
    path('admin/', TicketAdminView.as_view(), name='adminticketlist'),                # admin has access to all tickets
    path('admin/<int:pk>/', TicketAdminDetailView.as_view(), name='adminticketdetail'),
    path('pending/', TicketPendingView.as_view(), name='listpending'),
    path('closed/', TicketClosedView.as_view(), name='listclosed'),
    path('frozen/', TicketFrozenView.as_view(), name='listfrozen'),
    path('admin/frozen/', TicketAdminFrozenView.as_view(),  name='adminlistfrozen'),
    path('admin/pending/', TicketAdminPendingView.as_view(), name='adminlistpending'),
    path('admin/closed/', TicketAdminClosedView.as_view(), name='adminlistclosed'),
    path('<int:pk>/discuss/', DiscussionView.as_view(), name='discussticket'),
    path('admin/<int:pk>/discuss/', DiscussionAdminView.as_view(), name='admindiscussticket')
]