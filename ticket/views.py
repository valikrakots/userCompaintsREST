from django.shortcuts import render

from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ticket.models import Discussion, Ticket
from ticket.serializers import (DiscussionAdminSerializer,
                                DiscussionSerializer, TicketForAdminSerializer,
                                TicketSerializer)


# tickets view for simple user
class TicketList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer
    def get(self, request, format=None):

        tickets = Ticket.objects.all().filter(user=self.request.user)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ticket detail view for simple user
class TicketDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def get(self, request, pk):
        tickets = Ticket.objects.all().filter(user=self.request.user, ticket_id=pk)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            ticket = Ticket.objects.all().filter(user=self.request.user, ticket_id=pk).first()
            ticket.delete()
            discussions = Discussion.objects.all().filter(ticket=pk)
            for disc in discussions:
                disc.delete()
            return Response("Deleted", status=status.HTTP_200_OK)
        except:
            return Response("No such ticket", status=status.HTTP_400_BAD_REQUEST)


# ticket detail view for admin
class TicketAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Ticket.objects.all()
    serializer_class = TicketForAdminSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# list all pending tickets for simple user
class TicketPendingView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = TicketSerializer

    def get_queryset(self):
        username = self.request.user
        return Ticket.objects.all().filter(user=username, status='PENDING')


# list all frozen tickets for simple user
class TicketFrozenView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = TicketSerializer

    def get_queryset(self):
        username = self.request.user
        return Ticket.objects.all().filter(user=username, status='FROZEN')


# list all closed tickets for simple user
class TicketClosedView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = TicketSerializer

    def get_queryset(self):
        username = self.request.user
        return Ticket.objects.all().filter(user=username, status='CLOSED')


# list all closed tickets for admin
class TicketAdminClosedView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)

    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.all().filter(status='CLOSED')


# list all pending tickets for admin
class TicketAdminPendingView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.all().filter(status='PENDING')


# list all frozen tickets for admin
class TicketAdminFrozenView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.all().filter(status='FROZEN')


# list all tickets for admin
class TicketAdminView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


# discuss specific ticket for simple user
class DiscussionView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DiscussionSerializer

    def get(self, request, pk):
        if Ticket.objects.all().filter(ticket_id=pk).first().user == self.request.user:
            disc = Discussion.objects.all().filter(ticket=pk)
            serializer = DiscussionSerializer(disc, many=True)
            return Response(serializer.data)
        else:
            return Response(data="No such ticket for this user", status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk):
        serializer = DiscussionSerializer(data=request.data)
        try:
            last_issure = Discussion.objects.all().filter(ticket=pk).first().answer
            if last_issure is None:
                return  Response('You previous issue is not answered yet', status=status.HTTP_403_FORBIDDEN)
            elif Ticket.objects.all().filter(ticket_id=pk).first().status == 'CLOSED':
                return Response('The ticket is closed', status=status.HTTP_403_FORBIDDEN)
            else:
                raise Exception("Continue...")
        except:
            if serializer.is_valid():
                serializer.save(ticket=pk, answer=None)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response("You should provide question.", status=status.HTTP_400_BAD_REQUEST)


# discuss specific ticket for admin
class DiscussionAdminView(APIView):
    permission_classes = (IsAdminUser,)
    serialazer_class = DiscussionSerializer

    def get(self, request, pk):
        disc = Discussion.objects.all().filter(ticket=pk)
        serializer = DiscussionAdminSerializer(disc, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        issue = Discussion.objects.all().filter(ticket=pk).last()
        serializer = DiscussionAdminSerializer(issue, data=request.data)
        if serializer.is_valid() and issue != None:
            serializer.save()
            return Response(serializer.data)
        return Response("Nothing to discuss", status=status.HTTP_400_BAD_REQUEST)

    #def delete(self, request, pk, format=None):
    #    snippet = Discussion.objects.all().filter(ticket=pk)
    #    snippet.delete()
    #    return Response("Deleted" ,status=status.HTTP_204_NO_CONTENT)











