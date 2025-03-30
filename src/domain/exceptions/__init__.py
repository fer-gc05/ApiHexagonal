class DomainException(Exception):
    pass

class UserNotFoundException(DomainException):
    pass

class PostNotFoundException(DomainException):
    pass

class CommentNotFoundException(DomainException):
    pass

class InvalidCredentialsException(DomainException):
    pass