from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Livro
from . import serializers

@api_view(['GET', 'POST'])
def getLivros(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = serializers.LivroSerializer(livros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = serializers.LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def LivrosById(request, pk):
    try:
        livro = Livro.objects.get(id=pk)
    except Livro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        serializer = serializers.LivroSerializer(livro)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    if request.method == 'PUT':
        serializer = serializers.LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    if request.method == 'DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
