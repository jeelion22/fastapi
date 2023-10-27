from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint


class UserBase(BaseModel):
    email: EmailStr


class UserIn(UserBase):
    password: str
    phone_number: str | None = None


class UserOut(UserBase):
    id: int
    created_at: datetime
    phone_number: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostIn(PostBase):
    pass


class PostOut(PostIn):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut


class Token(BaseModel):
    access_token: str
    token_type: str


class Token_Data(BaseModel):
    id: str = None


class PostWithVote(BaseModel):
    Post: PostOut
    votes: int


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
