import requests

from posts_model import PostsModel

# from . import PostsModel
response_api = requests.get('https://jsonplaceholder.typicode.com/posts/1')

posts_1 = PostsModel(0, 0, '', '')