from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.comment import Comment

class CommentRepository(ABC):

    @abstractmethod
    def get_all_comments(self) -> List[Comment]:
        pass

    @abstractmethod
    def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        pass

    def get_comments_by_post_id(self, post_id: int) -> List[Comment]:
        pass

    @abstractmethod
    def create_comment(self, comment: Comment) -> Comment:
        pass

    @abstractmethod
    def update_comment(self, comment: Comment) -> Comment:
        pass

    @abstractmethod
    def delete_comment(self, comment_id: int) -> bool:
        pass