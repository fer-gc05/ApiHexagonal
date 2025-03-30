from src.application.ports.comment_repository import CommentRepository
from src.domain.exceptions import CommentNotFoundException

class DeleteComment:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, comment_id: int) -> bool:
        existing_comment = self.comment_repository.get_comment_by_id(comment_id)
        if not existing_comment:
            raise CommentNotFoundException('El comentario no existe')
        deleted = self.comment_repository.delete_comment(comment_id)
        if not deleted:
            raise Exception('No se pudo eliminar el comentario')
        return deleted