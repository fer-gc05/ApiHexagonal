from src.application.ports.post_repository import PostRepository

class DeletePost:

    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, post_id: int) -> bool:
        return self.post_repository.delete_post(post_id)