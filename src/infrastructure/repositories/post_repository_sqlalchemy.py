from src.domain.entities.post import Post
from src.application.ports.post_repository import PostRepository
from src.infrastructure.database.models.post import PostModel
from sqlalchemy.orm import Session

class PostRepositorySQLAlchemy(PostRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_post(self, post: Post) -> Post:
        db_post = PostModel(**post.model_dump(exclude={"id"}))
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return Post.model_validate(db_post)

    def get_post_by_id(self, post_id: int) -> Post:
        db_post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        if not db_post:
            raise ValueError('Post no encontrado')
        return Post.model_validate(db_post)

    def get_all_posts(self) -> list[Post]:
        db_posts = self.db.query(PostModel).all()
        return [Post.model_validate(post) for post in db_posts]

    def update_post(self, post_id: int, title: str, content: str) -> Post:
        db_post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        if not db_post:
            raise ValueError('Post no encontrado')
        db_post.title = title
        db_post.content = content
        self.db.commit()
        self.db.refresh(db_post)
        return Post.model_validate(db_post)

    def delete_post(self, post_id: int) -> bool:
        db_post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        if db_post:
            self.db.delete(db_post)
            self.db.commit()
            return True
        return False