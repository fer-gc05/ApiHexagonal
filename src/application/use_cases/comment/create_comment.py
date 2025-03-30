from src.domain.entities.comment import Comment
from src.application.ports.comment_repository import CommentRepository
from src.application.ports.post_repository import PostRepository
from src.domain.exceptions import PostNotFoundException

class CreateComment:
    def __init__(self, comment_repository: CommentRepository, post_repository: PostRepository):
        self.comment_repository = comment_repository
        self.post_repository = post_repository

    def execute(self, content: str, post_id: int, user_id: int) -> Comment:
        post = self.post_repository.get_post_by_id(post_id)
        if not post:
            raise PostNotFoundException('El post no existe')
        comment = Comment(content=content, post_id=post_id, user_id=user_id)
        created_comment = self.comment_repository.create_comment(comment)
        if not created_comment:
            raise Exception('No se pudo crear el comentario')
        return created_comment