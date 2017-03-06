from rest_framework import mixins, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LogSerializer


#this is a custom viewset for non-model based rest framework
class LogEntryViewSet(mixins.CreateModelMixin, viewsets.ViewSetMixin, APIView):
    serializer_class = LogSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.serializer_class
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def list(self, request):
        serializer = self.serializer_class(
            instance=[], many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        serializer = self.serializer_class(
            instance=None, context={'request': request})

        return Response(serializer.data)