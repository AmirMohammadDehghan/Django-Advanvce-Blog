from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins


data = {
  'id': 1,
  'title':'post'
}

'''
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def postList(request):
  if request.method == 'GET':
    post = Post.objects.filter(status=True)
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    return Response(serializer.data)




@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
  post = get_object_or_404(Post, pk=id, status=True)
  if request.method == 'GET':
    
    serializer = PostSerializer(post)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = PostSerializer(post, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  elif request.method == 'DELETE':
   post.delete() 
   return Response({'detail':'item removed successfully'})

      
   '''

"""class PostList(APIView):
  '''getting a list of posts and creating new posts'''
  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_class = PostSerializer
  def get(self, request):
    '''retrieving a list of posts'''
    post = Post.objects.filter(status=True)
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)


  def post(self, request):
    '''creating post with provided data'''
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    return Response(serializer.data)
"""

# @api_view()
# def postDetail(request, id):
#   try:
#     post = Post.objects.get(pk=id)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)
#   except Post.DoesNotExist:
#     return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

class PostList(ListCreateAPIView):
  '''getting a list of posts and creating new posts'''
  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_class = PostSerializer
  queryset = Post.objects.filter(status=True)

 





'''
class PostDetail(APIView):
  """getting detail of the post and edit plus removing it"""
  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_class = PostSerializer


  def get(self, request, id):
    """ retrieving the post data """
    post = get_object_or_404(Post, pk=id, status=True)
    serializer = self.serializer_class(post)
    return Response(serializer.data)


  def put(self, request, id):
    """ editing post data"""
    post = get_object_or_404(Post, pk=id, status=True)
    serializer = self.serializer_class(post, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


  def delete(self, request, id):
    """ deleting the post """
    post = get_object_or_404(Post, pk=id, status=True)
    post.delete() 
    return Response({'detail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)
'''

class PostDetail(RetrieveUpdateDestroyAPIView):
  """getting detail of the post and edit plus removing it"""
  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_class = PostSerializer
  queryset = Post.objects.filter(status=True)
  # lookup_field = 'id'


