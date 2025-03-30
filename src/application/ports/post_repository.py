from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.post import Post

class PostRepository(ABC):
    @abstractmethod
    def get_all_posts(self) -> List[Post]:
        pass

    @abstractmethod
    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        pass

    @abstractmethod
    def create_post(self, post: Post) -> Post:
        pass

    @abstractmethod
    def update_post(self, post_id: int, title: str, content: str) -> Post:
        pass

    @abstractmethod
    def delete_post(self, post_id: int) -> bool:
        pass