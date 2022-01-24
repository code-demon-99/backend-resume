from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

# return 404 status code
def error404(request,exception):
  exc = NotFound()
  return Response({'error':exc.detail}, status=status.HTTP_404_NOT_FOUND)
