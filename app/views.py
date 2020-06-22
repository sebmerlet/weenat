from rest_framework import viewsets

from .serializers import UsersSerializer, UsersDetailSerializer
from .models import Users


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        """
        Filter method using url parameter 'year'
        :return: queryset
        """
        year = self.request.query_params.get('year', None)
        if year:
            return Users.objects.filter(birthday__year=year)
        return Users.objects.all()

    def get_serializer_class(self):
        """
        Set serializer class on action type
        :return: Serializer class
        """
        if self.action == 'retrieve':
            return UsersDetailSerializer
        else:
            return UsersSerializer
