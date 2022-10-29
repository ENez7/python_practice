class PostsModel:
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body
    
    def __str__(self) -> str:
        return f'''User ID = {self.userId}
                Post ID = {self.id}
                Title = {self.title}
                Body = {self.body}'''
    
    def fromJson(self, json):
        self.userId = json['userId']
        self.id = json['id']
        self.title = json['title']
        self.body = json['body']