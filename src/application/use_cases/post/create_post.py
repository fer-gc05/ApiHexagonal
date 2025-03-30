from src.domain.entities.post import Post
from src.application.ports.post_repository import PostRepository

class CreatePost:

    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, title: str, content: str, user_id) -> Post:
        try:
            post = Post(title=title, content=content, user_id=user_id)
            created_post = self.post_repository.create_post(post)
            if not created_post:
                raise Exception('No se pudo crear el post')
            return created_post
        except Exception as e:
            raise e

