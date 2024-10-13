from sqlmodel import SQLModel, Field  # , TIMESTAMP
from datetime import datetime
from . import IDAutoIncrement


class Post(IDAutoIncrement, table=True):
    created_at: datetime = Field(default_factory=datetime.now)
    title: str = Field(nullable=False)
    content: str
