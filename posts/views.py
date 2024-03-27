from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from posts.serializers import PostSerializer
from posts.models import Post
from django.shortcuts import get_object_or_404





def get_post_by_id(posts, post_id):
    for post in posts:
        if post["id"] == post_id:
            return post
    return None

@api_view(http_method_names=['GET','POST'])
def homepage(request:Request):
    if request.method == 'POST':
        response = {
            'message': request.data
        }
        return Response(data=response,status=status.HTTP_201_CREATED)
    response = {
        'message': 'Posts Homepage',
    }
    return Response(data=response,status=status.HTTP_200_OK,)



class PostListCreateView(APIView):
    serializer_class = PostSerializer

    def get(self, request:Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(
            instance=posts,
            many=True
            )
        return Response(data = {
            'Message': 'Post Created',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    
    def post(self, request:Request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)





class PostRetrieveUpdateDeleteView(APIView):
    seriazlier_class = PostSerializer

    def get(self, request:Request, post_id: int):
        post = get_object_or_404(Post,pk=post_id)
        serializer = self.seriazlier_class(instance=post)
        return Response(data = serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request:Request, post_id: int):
        post = get_object_or_404(Post,pk=post_id)
        data = request.data

        serializer = self.seriazlier_class(instance=post,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={
                'message': 'Post Updated',
                'data': serializer.data
            }, status = status.HTTP_200_OK
            )
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request:Request, post_id: int):
        post = get_object_or_404(Post,pk=post_id)
        post.delete()
        return Response(data={
            'message': "Post Deleted",
            },
            status= status.HTTP_204_NO_CONTENT
            )


@api_view(http_method_names=['GET'])
def post_details(request:Request,post_id:int):
    post = get_object_or_404(Post,pk=post_id)
    serializer = PostSerializer(post)
    response = {
        'message': 'Post Created',
        'data': serializer.data
    }

    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=['PUT'])
def update_post(request:Request,post_id:int):
    post = get_object_or_404(Post, pk = post_id)
    data = request.data
    serializer = PostSerializer(
        instance = post,
        data = data
        )
    if serializer.is_valid():
        serializer.save()
        response = {
            'message': 'Post Updated',
            'data': serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['DELETE'])
def delete_post(request:Request,post_id:int):
    post = get_object_or_404(Post, pk = post_id)
    post.delete()
    
    return Response(data={
        'message': "Post Deleted",
    },status= status.HTTP_204_NO_CONTENT)