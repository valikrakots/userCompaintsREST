from rest_framework import serializers

from ticket.models import Discussion, Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('title', 'ticket_id', 'user', 'status', 'content', 'created', 'modified', 'answer')
        read_only_fields = ['user']
        extra_kwargs = {"answer": {"required": False, "allow_null": True}}

class TicketForAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('title', 'ticket_id', 'user', 'status', 'content', 'created', 'modified', 'answer')
        extra_kwargs = {"title": {"required": False, "allow_null": True}, "content": {"required": False},}


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = ('answer', 'question', 'ticket', 'created')
        extra_kwargs = {"answer": {"required": False}}
        read_only_fields = ['ticket']


class DiscussionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = ('answer', 'question', 'ticket', 'created')
        extra_kwargs = {"question": {"required": False, "allow_null": True}}
        read_only_fields = ['ticket']

