from src.domain.entities.comment import Comment
from src.application.ports.comment_repository import CommentRepository
from src.infrastructure.database.models.comment import CommentModel
from sqlalchemy.orm import Session

class CommentRepositorySQLAlchemy(CommentRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_comment(self, comment: Comment) -> Comment:
        db_comment = CommentModel(**comment.model_dump(exclude={"id"}))
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return Comment.model_validate(db_comment)

    def get_comment_by_id(self, comment_id: int) -> Comment | None:
        db_comment = self.db.query(CommentModel).filter(CommentModel.id == comment_id).first()
        return Comment.model_validate(db_comment) if db_comment else None

    def get_comments_by_post_id(self, post_id: int) -> list[Comment]:
        db_comments = self.db.query(CommentModel).filter(CommentModel.post_id == post_id).all()
        return [Comment.model_validate(comment) for comment in db_comments]

    def get_all_comments(self) -> list[Comment]:
        db_comments = self.db.query(CommentModel).all()
        return [Comment.model_validate(comment) for comment in db_comments]

    def update_comment(self, comment: Comment) -> Comment:
        db_comment = self.db.query(CommentModel).filter(CommentModel.id == comment.id).first()
        if db_comment:
            for key, value in comment.model_dump(exclude={"id"}).items():
                setattr(db_comment, key, value)
            self.db.commit()
            self.db.refresh(db_comment)
            return Comment.model_validate(db_comment)
        return comment

    def delete_comment(self, comment_id: int) -> bool:
        db_comment = self.db.query(CommentModel).filter(CommentModel.id == comment_id).first()
        if db_comment:
            self.db.delete(db_comment)
            self.db.commit()
            return True
        return False