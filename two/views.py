from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class InfoView(APIView):
    permission_classes = [permissions.AllowAny,]

    def get(self, request):
        json = {
            'register': '/api/token/create/     (post: provide email and password)',
            'get_token': '/api/token/obtain/        (post: provide email and password)',
            'refresh_token': '/api/token/refresh/       (post: provide refresh token)',
            'WARNING!!!':  'to view following urls you should provide Authentication field that contains' +
                           ' your ACCESS TOKEN(put JWT in the beginning)',
            '(post/get)_tickets': '/api/tickets/        (post: provide title and content, get: no pars needed)',
            'get_tickets_with_status': '/api/tickets/{status}/      (get: no pars needed)',
            'view_ticket_detail': '/api/tickets/{ticket_id}/        (get: no pars needed)',
            '(view/post)_comment_for_ticket': '/api/tickets/{ticket_id}/discuss/  (post: provide question, get: no ' +
                                              'pars needed)',
        }
        return Response(data=json, status=status.HTTP_200_OK)



class InfoAdminView(APIView):
    permission_classes = [permissions.IsAdminUser,]

    def get(self, request):
        json = {
            'WARNING!!!':  'to view following urls you should provide Authentication field that contains' +
                           ' your ACCESS TOKEN(put JWT in the beginning)',
            'get_tickets': '/api/tickets/admin/        (get: no pars needed)',
            '(view/put)_ticket_detail': '/api/tickets/admin/{ticket_id}/        (get: no pars needed, put: provide answer',
            '(view/put)_comment_for_ticket': '/api/tickets/admin/{ticket_id}/discuss/  (post: provide answer, get: no ' +
                                              'pars needed)',
            'get_tickets_with_status': '/api/tickets/admin/{status}/      (get: no pars needed)',
        }
        return Response(data=json, status=status.HTTP_200_OK)
