from rest_framework.response import Response
from rest_framework import status
from .serializers import BooksSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import generics
from ..models import bookStore
from rest_framework import viewsets



class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.group.filter(name='viewr').exist()


@api_view(['POST'])
def Create(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'message': 'book created',
            'success': True
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        'Error': serializer.errors,
        'success': False
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def apiSignup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'message': 'user added',
            'success': True
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        'Error': serializer.errors,
        'success': False
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def index(request):
    books = bookStore.objects.all()
    serializer = BooksSerializer(instance=books, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def delete(request,id):
    book = bookStore.objects.get(pk=id)
    serializer = BooksSerializer(instance=book, many=False)
    serializer.delete()
    return Response(data={
        'message': 'deleted',
        'success': True
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def update(request,id):
    book = bookStore.objects.get(pk=id)
    serializer = BooksSerializer(instance=book, many=False,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'message': 'book updated',
            'success': True
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        'Error': serializer.errors,
        'success': False
    }, status=status.HTTP_400_BAD_REQUEST)



