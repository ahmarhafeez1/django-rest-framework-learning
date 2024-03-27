from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from posts.serializers import PostSerializer
from posts.models import Post



posts = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the content of the first post."
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the content of the second post."
    },
    {
        "id": 3,
        "title": "Third Post",
        "content": "This is the content of the third post."
    }
]

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



@api_view(http_method_names=['GET','POST'])
def list_posts(request:Request):
    if(request.method == 'POST'):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={
                'message': 'Post Created',
                'data': serializer.data,
            },
            status=status.HTTP_201_CREATED
            )
        
    posts = Post.objects.all()
    serializer = PostSerializer(
        instance = posts, 
        many = True
        )
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def post_details(request:Request,post_id:int):
    try:
         
        post = Post.objects.get(id = post_id)
        serializer = PostSerializer(
            instance=post
        )
        return Response(data=serializer.data)
    except:
        return Response(data={"error": "Post Not Found",},status=status.HTTP_404_NOT_FOUND)