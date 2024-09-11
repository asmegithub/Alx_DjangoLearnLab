from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework
from datetime import datetime

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter

# this view is to list all the books


class ListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filtering and ordering by title and publication year
    # filter_backends = [filters.SearchFilter,
    #                    filters.OrderingFilter]
    filter_backends = [rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    # filtering book
    filterset_class = BookFilter
    # ordering book by title and publication year
    ordering_fields = ['title', 'publication_year']
    # searching book by title and publication year
    search_fields = ['title', 'author__name', 'publication_year']

    # this is to make sure that only authenticated users can access this view
    # permission_classes = [IsAuthenticated]

    # this is to filter the books by their publication_year and return only the books that were published in the current year
    # def get_queryset(self):
    #     queryset = Book.objects.all().filter(publication_year=datetime.now().year)
    #     return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Seeing the detail of a book


class DetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # this is to make sure that only authenticated users can access this view
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# Registering new book


class CreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # this is to make sure that only authenticated admin users can access this view
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        # this is to make sure that the publication year is not greater than the current year. Similar validation has been done in the serializer but it is always good to have it in the view as well
        if request.data.get('publication_year') > datetime.now().year:
            return Response({'error': 'Publication year must be before or equal to the current year'}, status=400)
        return self.create(request, *args, **kwargs)

# Updating a book


class UpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # this is to make sure that only authenticated admin users can access this view
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        # this is to make sure that the publication year is not greater than the current year. Similar validation has been done in the serializer but it is always good to have it in the view as well
        if request.data.get('publication_year') > datetime.now().year:
            return Response({'error': 'Publication year must be before or equal to the current year'}, status=400)
        return self.update(request, *args, **kwargs)


class DeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # this is to make sure that only authenticated admin users can access this view
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
