from src.domain.entities.post import Post
from src.application.ports.post_repository import PostRepository
from src.domain.exceptions import PostNotFoundException

class UpdatePost:

    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, post_id: int, title: str, content: str) -> Post:
        try:
            updated_post = self.post_repository.update_post(post_id, title, content)
            if not updated_post:
                raise Exception("No se pudo actualizar el post")
            return updated_post
        except ValueError:
            raise PostNotFoundException(f"Post con ID {post_id} no encontrado")
        except Exception as e:
            raise Exception(f"Error al actualizar el post: {str(e)}")